class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for index in range(0, len(haystack)-len(needle)+1):
            if haystack[index: index + len(needle)] == needle:
                return index
        return -1  