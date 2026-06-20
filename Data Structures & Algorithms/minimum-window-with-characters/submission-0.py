class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT = {}
        window = {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        have = 0
        need = len(countT)
        res = [-1, -1]
        length = float("infinity")
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)
            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:
                if (r - l + 1) < length:
                    res = [l, r]
                    length = (r - l + 1)
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1


        l, r = res
        if length != float("infinity"):
            return s[l: r+1]
        else:
            return ""