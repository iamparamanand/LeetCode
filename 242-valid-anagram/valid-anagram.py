class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s.lower()) == sorted(t.lower())
        if(len(t) != len(s)):
            return False
        dictT,dictS = {},{}
        for i in range(len(t)):
            dictT[t[i]] = 1+ dictT.get(t[i],0)
            dictS[s[i]] = 1+ dictS.get(s[i],0)

        return dictT == dictS

#Another solution using sorted function
        # len_s = len(s)
        # len_t = len(t)
        # s = sorted(s) 
        # t = sorted(t)
        # if len_s == len_t:
        #     for i in range(0,len_s):
        #         while s[i] != t[i]:
        #             return False
        
        #     return True