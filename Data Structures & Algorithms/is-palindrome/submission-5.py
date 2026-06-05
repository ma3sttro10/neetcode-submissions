import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans('', '', string.punctuation))
        s = s.replace(" ","").lower()
        if s == s[::-1]:
            return True
        else :
            return False