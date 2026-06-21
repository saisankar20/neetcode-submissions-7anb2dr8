class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        w_count = {}
        min_len = float("inf")
        result = (-1, -1)
        l = 0
        have = 0
        need = len(t_count)

        for r in range(len(s)):
            c = s[r]
            w_count[c] = w_count.get(c, 0) + 1  # increment from w_count

            # check if this char now satisfies t's requirement
            if c in t_count and w_count[c] == t_count[c]:
                have += 1

            # shrink from the left while window is valid
            while have == need:
                # update result if this window is smaller
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    result = (l, r)

                # remove leftmost char
                w_count[s[l]] -= 1
                if s[l] in t_count and w_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1

        l, r = result
        return s[l:r+1] if min_len != float("inf") else ""