class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s) - 1
        res , c = 0, 0
        symbol = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        while c <= n:
            if s[c] in symbol:
                if c == n:
                    res += symbol[s[c]]
                elif symbol[s[c+1]] <= symbol[s[c]]:
                        res += symbol[s[c]]
                else:
                    res = res - symbol[s[c]]
                c += 1
            else:
                return -1

        return res
        