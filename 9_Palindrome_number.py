class Solution:
    def isPalindrome(self, x: int) -> bool:
        text = str(x)
        for i in range(len(text)//2):
            if text[i] != text[-(i+1)]:
                return False
        return True

        