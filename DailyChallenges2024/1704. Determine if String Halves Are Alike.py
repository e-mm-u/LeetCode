class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        i,j = 0,len(s)-1
        s = s.lower()
        numOfVowelFirstHalf, numOfVowelSecondHalf= 0,0
        while i<j:
            if(s[i] in ('a', 'e', 'i', 'o', 'u')):
                numOfVowelFirstHalf += 1
            if(s[j] in ('a', 'e', 'i', 'o', 'u')):
                numOfVowelSecondHalf += 1
            
            i,j = i+1, j-1
        
        return numOfVowelFirstHalf==numOfVowelSecondHalf
