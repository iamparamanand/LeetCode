class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s, seen_t = {}, {}
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] not in seen_s:
                    seen_s[s[i]] = 1
                seen_s[s[i]] += 1
                if t[i] not in seen_t:
                    seen_t[t[i]] = 1
                seen_t[t[i]] += 1
            res = all([seen_s.get(key) == value for key, value in seen_t.items()])
            return res
        return False