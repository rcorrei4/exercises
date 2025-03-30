from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             k = target - nums[i]
#             for j in range(len(nums)):
#                 if k == nums[j] and j != i:
#                     return [i, j]

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap = {}
        
#         for i in range(len(nums)):
#             print(i)
#             if target-nums[i] in hashmap.values():
#                 return [i, nums.index(target-nums[i])]
            
#             hashmap[i] = nums[i]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i