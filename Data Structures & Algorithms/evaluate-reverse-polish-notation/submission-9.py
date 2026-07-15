class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        c = int(tokens[0])
        s = []
        for i in range(len(tokens)):
            d = tokens[i]
            if d.lstrip("-").isnumeric():
                s.append(int(d))
            else:
                if d=="+":
                    e = s[-1]+s[-2]
                    s.pop()
                    s[-1] = e
                elif d=="-":
                    e = s[-2]-s[-1]
                    s.pop()
                    s[-1] = e
                elif d=="*":
                    e = s[-1]*s[-2]
                    s.pop()
                    s[-1] = e
                elif d=="/":
                    e = int(s[-2]/s[-1])
                    s.pop()
                    s[-1] = e
        return s[0]
                    