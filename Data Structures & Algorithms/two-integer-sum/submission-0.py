from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        store = dict()
        for i in range(n):
            if nums[i] in store:
                return [store[nums[i]], i] 
            else:
                store[target - nums[i]] = i
        return [-1, -1]

        
        