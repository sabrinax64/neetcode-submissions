class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = nums * 2 #is this how I address nums? 


        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans