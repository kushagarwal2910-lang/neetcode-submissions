class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for i in strs:
            t = str(sorted(list(i)))
            if t in m:
                m[t].append(i)
            else:
                m[t] = [i]
        return list(m.values())