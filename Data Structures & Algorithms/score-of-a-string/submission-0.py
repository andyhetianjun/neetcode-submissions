class Solution:
    def scoreOfString(self, s: str) -> int:
        arr = [ord(char) for char in s]

        amount = 0 

        for i in range(len(arr) - 1):
            amount += abs(arr[i] - arr[i + 1])
        
        return amount