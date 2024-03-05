class Solution:
    def isPalindrome(self, s: str) -> bool:
        len_s = len(s)
        string = ""
        for chr in s:
            if chr.isalpha():
               string += chr
            if chr.isdigit():
                string+= chr
        string = string.lower()
        if string == string[::-1]:
            return True
        else:
            return False