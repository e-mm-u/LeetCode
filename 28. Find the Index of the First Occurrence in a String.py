class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        n_len, h_len = len(needle), len(haystack)
        
        for i in range(h_len-n_len+1):
            if haystack[i] == needle[0]:
                matched = False
                for j in range(n_len):
                    if needle[j] != haystack[i+j]:
                        matched = False
                        break
                    else:
                        matched = True
                if matched :
                    return i
        return -1