class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            leftout = target - nums[i]
            if leftout in seen:
                return [seen[leftout], i]
            seen[nums[i]] = i
        