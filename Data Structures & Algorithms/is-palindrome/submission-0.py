class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=[i.lower() for i in s if i.isalnum()]
        return new ==new[::-1]
        