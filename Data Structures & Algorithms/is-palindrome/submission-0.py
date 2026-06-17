class Solution:
    def isPalindrome(self, s: str) -> bool:
       cleaned_s = "".join(char.lower() for char in s if char.isalnum()) 
       rev_s = cleaned_s[::-1]
       if cleaned_s == rev_s:

        return True
       return False 
