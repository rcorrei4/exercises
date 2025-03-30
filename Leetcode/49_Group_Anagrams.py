from collections import defaultdict
from typing import List

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         hashmap = defaultdict(list)
        
#         for word in strs:
#             word_hashmap = {}
#             for char in word:
#                 word_hashmap[char] = word_hashmap.get(char, 0) + 1

#             word_list = []
#             for key, val in word_hashmap.items():
#                 word_list.append(key+str(val))
#             word_list = sorted(word_list)
            
#             hashmap[tuple(word_list)].append(word)
            
#         return list(hashmap.values())

class Solution: 
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
		ans = defaultdict(list) 
		for s in strs: 
			count = [0] * 26 
			for c in s: 
				count[ord(c) - ord('a')] += 1 
			ans[tuple(count)].append(s) 
		return ans.values()