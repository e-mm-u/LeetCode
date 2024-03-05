class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s)==1:
            return 1
        if s[0]!=s[len(s)-1]:
            return len(s)

        start, end = 0, len(s)-1

        while start<end and s[start]==s[end]:
            cut = s[start]
            while start<=end and s[start]==cut:
                start += 1
            while start<=end and s[end]==cut:
                end -= 1
        
        return end-start+1