class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = 0
        hashtable = {}
    
        for i, c in enumerate(nums):
            hashtable[str(i)] = c
        
        while counter < len(nums)-1:
            tosearch = target - nums[counter]
            index = None
            for k,v in hashtable.items():
                if tosearch == v:
                    index = int(k)
            if index and index != counter:
                return [counter, index]
            else:
                counter +=1