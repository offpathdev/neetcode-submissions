class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # # optimised brute force solution
        # # req: compare two elements - two loops
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        # optimised solution
        store = set()
        for num in nums:
            if num in store:
                return True
            store.add(num)
        return False
