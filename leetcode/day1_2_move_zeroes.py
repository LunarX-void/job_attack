# 283. 移动零 - LeetCode
# 状态: 待提交
# 思路: 双指针，慢指针指向下一个非零元素应该放的位置

from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    原地修改，不返回任何值
    """
    # 请在这里写你的代码
    # left = 0
    # for right in range(len(nums)):
    #     if nums[right] != 0:
    #         nums[left], nums[right] = nums[right], nums[left]
    #         left += 1
    # 不需要返回，nums 已被原地修改

# 本地测试
if __name__ == '__main__':
    # 测试用例1
    nums1 = [0, 1, 0, 3, 12]
    moveZeroes(nums1)
    print(nums1)  # 期望输出 [1, 3, 12, 0, 0]

    # 测试用例2
    nums2 = [0]
    moveZeroes(nums2)
    print(nums2)  # 期望输出 [0]