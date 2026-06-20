class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {")": "(", "}":"{", "]":"["}
        if len(s) % 2 == 1:
            return False
        for char in s:
            if char in map:
                if stack and stack[-1] == map[char]:
                    stack.pop()
                else:
                    return False 

            else:
                stack.append(char)
        if not stack:
            return True
        else:
            return False