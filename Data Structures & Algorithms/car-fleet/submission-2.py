class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        m = sorted(zip(position,speed), reverse=True)
        k = []
        for i in range(len(m)):
            d = (target-m[i][0])/m[i][1]
            k.append(d)
            if len(k)>=2 and k[-1]<=k[-2]:
                k.pop()
        return len(k)