# 206. 反转链表 - LeetCode
# 状态: 待提交
# 思路: 迭代法，prev/curr/next 三个指针

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    反转链表，返回新头节点
    """
    # # 请在这里写你的代码
    # prev = None
    # curr = head
    # while curr:
    #     next_temp = curr.next  # 先存一下下一个节点
    #     curr.next = prev  # 反转指针
    #     prev = curr  # 前指针后移
    #     curr = next_temp  # 当前指针后移
    # return prev


# 本地测试（数组转链表，链表转数组 的工具函数）
def build_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linked_list_to_array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


if __name__ == '__main__':
    # 测试用例: [1,2,3,4,5] -> [5,4,3,2,1]
    head = build_linked_list([1, 2, 3, 4, 5])
    reversed_head = reverseList(head)
    print(linked_list_to_array(reversed_head))  # 期望输出 [5,4,3,2,1]

    # 测试用例: [] -> []
    head2 = build_linked_list([])
    reversed_head2 = reverseList(head2)
    print(linked_list_to_array(reversed_head2))  # 期望输出 []