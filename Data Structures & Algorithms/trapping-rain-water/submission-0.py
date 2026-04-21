class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l , r = 0, len(height) - 1
        lm, rm = height[l], height[r]
        water = 0

        while l < r:
            if lm < rm:
                l += 1
                lm = max(lm, height[l])
                water += lm - height[l]
            else:
                r -= 1
                rm = max(rm, height[r])
                water += rm - height[r]
        return water
