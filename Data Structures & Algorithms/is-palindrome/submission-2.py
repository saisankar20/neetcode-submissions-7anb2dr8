class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        s = ''.join(char.lower() for char in s if char.isalnum())
        if not s:
            return True
        n = len(s)
        for i in range(len(s)):
            if s == s[::-1]:
                return True
            else:
                return False