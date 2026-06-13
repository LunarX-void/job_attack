# 工业串口调试助手

## 项目简介
工业现场常用的串口调试工具，基于 Python + PyQt5 开发。实现串口扫描、参数配置、数据收发、接收区实时显示等核心功能，并**预留了 Modbus 等工业协议扩展接口**。

## 技术栈
- Python 3.10
- PyQt5（GUI 框架）
- pyserial（串口通信库）
- 多线程（防止界面卡顿）

## 主要功能
- 自动扫描并列出可用 COM 端口
- 支持多种波特率（9600/19200/115200）
- 串口打开/关闭、数据发送、接收区实时显示
- **协议扩展**：支持“透明传输”和“简单问答协议(演示)”，预留 Modbus RTU 接口

## 运行方式
```bash
# 安装依赖
pip install pyqt5 pyserial

# 进入项目目录
cd job_attack

# 运行程序
python projects/serial_assistant.py