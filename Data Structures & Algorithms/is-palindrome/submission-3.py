class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = s.split()
        c = "".join(c)
        k = []
        for i in c:
            if i.isalnum():
                k.append(i.lower())
        k = "".join(k)
        i = 0
        j = len(k)-1
        while i<j:
            if k[i]!=k[j]:
                return False
            i+=1
            j-=1
        return True