class Solution:
    def isPalindrome(self, x: int) -> bool:
        text = str(x)
        for index, letter in enumerate(text):
            if letter != text[-(index+1)]:
                return False
        return True

        