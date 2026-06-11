# 21. 合并两个有序链表 - LeetCode
# 状态: 待提交
# 思路: 迭代法，使用哨兵节点简化边界

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    合并两个升序链表，返回新链表头节点
    """
    # 伪代码结构
    # dummy = ListNode()  # 哨兵节点，永远站在最前面
    # current = dummy
    #
    # while list1 and list2:
    #     if list1.val <= list2.val:
    #         current.next = list1
    #         list1 = list1.next
    #     else:
    #         current.next = list2
    #         list2 = list2.next
    #     current = current.next
    #
    # # 把剩余链表接上(条件为真取表达式1，条件为假取表达式2：结果=表达式1 if判断条件 else 表达式2）
    # current.next = list1 if list1 else list2
    #
    # return dummy.next


# 本地测试工具函数
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
    # 测试用例1: [1,2,4] + [1,3,4] -> [1,1,2,3,4,4]
    l1 = build_linked_list([1, 2, 4])
    l2 = build_linked_list([1, 3, 4])
    merged = mergeTwoLists(l1, l2)
    print(linked_list_to_array(merged))

    # 测试用例2: [] + [] -> []
    print(linked_list_to_array(mergeTwoLists(None, None)))

    # 测试用例3: [] + [0] -> [0]
    l3 = build_linked_list([])
    l4 = build_linked_list([0])
    print(linked_list_to_array(mergeTwoLists(l3, l4)))