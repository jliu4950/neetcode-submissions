class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        end = -1
        str_len = 0

        i = 0
        while i < len(s):
            if s[i] == "#":
                start = i + 1
                str_len = int(s[end + 1: i])
                res.append(s[start:start + str_len])
                end = start + str_len - 1
                i = end + 1
            else:
                i = i + 1

        return res