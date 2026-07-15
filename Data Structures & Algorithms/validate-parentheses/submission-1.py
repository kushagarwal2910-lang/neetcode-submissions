class Solution:
    def isValid(self, s: str) -> bool:
        d = []
        k = {"}":"{", "]":"[", ")":"("}
        for i in range(len(s)):
            if s[i] in k and d and k[s[i]]==d[-1]:
                d.pop()
            else:
                d.append(s[i])

        if len(d)==0:
            return True
        else:
            return False