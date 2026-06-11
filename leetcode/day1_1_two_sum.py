# 1. 两数之和 - LeetCode
# 已通过 LeetCode 验证

def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return []

# 本地测试（与 LeetCode 判题逻辑一致）
if __name__ == '__main__':
    print(twoSum([2,7,11,15], 9))   # [0,1]
    print(twoSum([3,2,4], 6))       # [1,2]
    print(twoSum([3,3], 6))         # [0,1]