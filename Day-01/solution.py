class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x) #convert number to string
        return s == s[::-1] #compare with its reversed string
