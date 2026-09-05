class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        most = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = most
            most =  max(most, temp)              
        return arr