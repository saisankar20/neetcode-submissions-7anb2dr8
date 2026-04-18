class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = []
        for i in range(len(nums)):
            x = 1
            for val in nums[:i] + nums[i+1:]:
                x *= val
            sol.append(x)
        return sol