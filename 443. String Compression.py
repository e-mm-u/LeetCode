class Solution:
    def compress(self, chars: List[str]) -> int:
        length = len(chars)
        start = 0
        pos = 0

        while start<length:
            count = 1
            while start+1<length and chars[start]==chars[start+1]:
                count += 1
                start += 1
            
            chars[pos] = chars[start]
            pos += 1
            if count>1:
                for c in str(count):
                    chars[pos] = c
                    pos += 1
            start += 1

        return pos