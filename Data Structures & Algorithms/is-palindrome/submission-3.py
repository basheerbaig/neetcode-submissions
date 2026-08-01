class Solution:
    def isPalindrome(self, s: str) -> bool:

        newStr = ""

        for c in s:
            if c.isalnum(): # to eliminate special char and spaces 
                newStr += c.lower() # making it all lower case 
        return newStr == newStr[::-1]

        