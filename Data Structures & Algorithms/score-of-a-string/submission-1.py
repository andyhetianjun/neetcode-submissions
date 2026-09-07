class Solution:
    def scoreOfString(self, s: str) -> int:
        amount = 0 

        for i in range(len(s) - 1):
            amount += abs(ord(s[i]) - ord(s[i + 1]))
        
        return amount