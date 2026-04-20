class Solution:
    def threeSum(self, nums):
        nums.sort()          # Array ko sort kar diya
        ans = []             # Answer list

        for i in range(len(nums) - 2):     # Ek number fix
            if i > 0 and nums[i] == nums[i - 1]:
                continue                  # Duplicate skip

            left = i + 1                  # Left pointer
            right = len(nums) - 1         # Right pointer

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:                # Sum zero mila
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

                elif s < 0:               # Sum chhota hai
                    left += 1
                else:                     # Sum bada hai
                    right -= 1

        return ans