# 704. 二分查找 - LeetCode
# 状态: 待提交
# 思路: 标准二分查找，左闭右闭区间 [left, right]

from typing import List

def search(nums: List[int], target: int) -> int:
    """
    在有序数组中查找目标值，返回索引，不存在返回 -1
    """
    # left, right = 0, len(nums) - 1  # 注意 right 初始值
    #
    # while left <= right:  # 注意是 <=，因为 left==right 时区间还有效
    #     mid = left + (right - left) // 2  # 防止溢出
    #     if nums[mid] == target:
    #         return mid
    #     elif nums[mid] < target:
    #         left = mid + 1
    #     else:
    #         right = mid - 1
    #
    # return -1

# 本地测试
if __name__ == '__main__':
    # 测试用例1
    print(search([-1,0,3,5,9,12], 9))   # 期望输出 4
    # 测试用例2
    print(search([-1,0,3,5,9,12], 2))   # 期望输出 -1
    # 测试用例3
    print(search([5], 5))               # 期望输出 0