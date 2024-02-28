class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
#Second Approach
        # a = dict()
        # for i in range(len(strs)):
        #     b = "".join(sorted(strs[i]))
        #     if b not in a:
        #         a[b] = [strs[i]]
        #     else:
        #         a[b].append(strs[i])
        # return a.values()