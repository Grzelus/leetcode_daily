class Solution:
    def isPalindrome(self, x: int) -> bool:
        text = str(x)
        if text == text[::-1]:
            return True
        return False
        