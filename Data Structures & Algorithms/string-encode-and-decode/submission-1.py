class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeStr = ""
        for s in strs:
            encodeStr = encodeStr + str(len(s)) + "#" + s
        return encodeStr
        
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            delimiter = s.find("#", i)
            length = int(s[i:delimiter])
            res.append(s[delimiter + 1 : delimiter + 1 + length])
            i = delimiter + 1 + length
        return res