from collections import defaultdict
from typing import List

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         hashmap = defaultdict(int)
        
#         for num in nums:
#             hashmap[num] += 1
            
#         result = [x for x in range(1, k+1)]
#         for i in range(k):
#             for num in hashmap.keys():
#                 if hashmap[num] > hashmap.get(result[i], 0) and num not in result:
#                     result[i] = num
                    
#         return result

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()
        
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
            
        result = [[] for _ in range(len(nums)+1)]
        
        for num, count in hashmap.items():
            result[count].append(num)
            
        result_top = []
            
        for i in result[::-1]:
            for j in i:
                result_top.append(j)
                if len(result_top) == k:
                    return result_top