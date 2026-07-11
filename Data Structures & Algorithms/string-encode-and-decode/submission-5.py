class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            s = "se"
            return s
        else:
            s = ";".join(strs)
            return s
       
    def decode(self, s: str) -> List[str]:
        if s == "se":
            return []
        strs = s.split(";")
        return strs