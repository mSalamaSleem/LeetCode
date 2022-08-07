class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = {}
        for i in range(len(nums)):
            if res.get(nums[i]) == None:
                res[nums[i]] = 1
            else:
                return True
        return False