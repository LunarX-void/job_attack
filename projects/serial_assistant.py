
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'C:\Users\谢\Desktop\job_attack\venv\Lib\site-packages\PyQt5\Qt5\plugins'
import sys
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class SerialAssistant(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ser = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('工业串口调试助手')
        self.setGeometry(300, 300, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 第一行：端口/波特率/打开按钮
        h_layout1 = QHBoxLayout()
        self.port_combo = QComboBox()
        self.baud_combo = QComboBox()
        self.baud_combo.addItems(['9600', '19200', '115200'])
        self.open_btn = QPushButton('打开串口')
        self.open_btn.clicked.connect(self.toggle_serial)
        h_layout1.addWidget(QLabel('端口:'))
        h_layout1.addWidget(self.port_combo)
        h_layout1.addWidget(QLabel('波特率:'))
        h_layout1.addWidget(self.baud_combo)
        h_layout1.addWidget(self.open_btn)
        # 添加协议选择下拉框
        self.protocol_combo = QComboBox()
        self.protocol_combo.addItems(['透明传输', '简单问答协议(演示)', 'Modbus RTU (预留)'])
        h_layout1.addWidget(QLabel('协议：'))
        h_layout1.addWidget(self.protocol_combo)

        h_layout1.addStretch()
        layout.addLayout(h_layout1)

        # 接收区
        layout.addWidget(QLabel('接收区:'))
        self.recv_text = QTextEdit()
        self.recv_text.setReadOnly(True)
        layout.addWidget(self.recv_text)

        # 发送区
        layout.addWidget(QLabel('发送区:'))
        self.send_edit = QTextEdit()
        layout.addWidget(self.send_edit)

        # 发送按钮
        self.send_btn = QPushButton('发送数据')
        self.send_btn.clicked.connect(self.send_data)
        layout.addWidget(self.send_btn)

        # 刷新端口列表
        self.refresh_ports()

    def refresh_ports(self):
        # 获取可用串口列表
        ports = serial.tools.list_ports.comports()
        self.port_combo.clear()
        for port in ports:
            self.port_combo.addItem(port.device)

    def toggle_serial(self):
        if self.ser is None or not self.ser.is_open:
            # 打开串口
            try:
                port = self.port_combo.currentText()
                baud = int(self.baud_combo.currentText())
                self.ser = serial.Serial(port, baud, timeout=0.5)
                self.open_btn.setText('关闭串口')
                self.recv_text.append(f'已打开 {port} 波特率 {baud}')
            except Exception as e:
                self.recv_text.append(f'打开失败: {str(e)}')
        else:
            # 关闭串口
            self.ser.close()
            self.ser = None
            self.open_btn.setText('打开串口')
            self.recv_text.append('串口已关闭')

    def send_data(self):
        if self.ser is None or not self.ser.is_open:
            self.recv_text.append('请先打开串口')
            return

        protocol = self.protocol_combo.currentText()
        raw_data = self.send_edit.toPlainText().strip()

        if not raw_data:
            return

        if protocol == '透明传输':
            send_bytes = raw_data.encode('utf-8')
            self.recv_text.append(f'发送(透明): {raw_data}')

        elif protocol == '简单问答协议(演示)':
            # 自定义协议：输入 GET_TEMP 返回模拟温度
            if raw_data == 'GET_TEMP':
                send_bytes = b'\x01\x03\x00\x00\x00\x01\x84\x0A'  # 示例Modbus读温度
                self.recv_text.append('[协议] 发送读取温度指令')
                # 模拟接收回复（实际应该在线程中读串口，这里简化演示）
                from threading import Timer
                def fake_reply():
                    self.recv_text.append('[模拟回复] 温度: 25.6°C')

                Timer(0.2, fake_reply).start()
            elif raw_data == 'GET_STATUS':
                send_bytes = b'\x01\x03\x00\x01\x00\x01\xD5\xCA'
                self.recv_text.append('[协议] 发送读取状态指令')
                Timer(0.2, lambda: self.recv_text.append('[模拟回复] 状态: 正常')).start()
            else:
                self.recv_text.append('[协议] 未知命令，可用: GET_TEMP, GET_STATUS')
                return
        else:  # Modbus预留或其他
            send_bytes = raw_data.encode('utf-8')
            self.recv_text.append(f'发送(默认): {raw_data}')

        self.ser.write(send_bytes)
        self.send_edit.clear()
    def closeEvent(self, event):
        if self.ser and self.ser.is_open:
            self.ser.close()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SerialAssistant()
    window.show()
    sys.exit(app.exec_())