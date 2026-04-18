class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            length = len(s)
            encoded += str(length) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Find delimiter '#'
            j = i
            while s[j] != '#':
                j += 1
            # Get length
            length = int(s[i:j])
            # Move i to start of string (after '#')
            i = j + 1
            # Extract string
            res.append(s[i:i+length])
            # Move i to next length indicator
            i += length
        return res