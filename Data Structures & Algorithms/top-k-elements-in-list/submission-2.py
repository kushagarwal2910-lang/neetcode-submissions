class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for i in nums:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        r = dict(sorted(m.items(), key = lambda x:x[1], reverse=True))
        l = list(r.keys())
        l = [l[y] for y in range(k)]
        return l
