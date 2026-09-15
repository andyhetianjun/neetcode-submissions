class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            word = ""
            domain = False
            c = 0 
            while email[c] != "@":
                if email[c] == "+":
                    while email[c] != "@":
                        c += 1 
                    break
                if email[c] != ".":
                    word += email[c]

                c += 1
            
            word += email[c:]
            unique.add(word)
        return len(unique)
            