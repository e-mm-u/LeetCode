class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        sortedStr = ''.join(sorted(s, reverse=True))
        for i in range(len(sortedStr)-1, -1, -1):
            if sortedStr[-1]!='1' and sortedStr[i] == '1':
                sortedStr = sortedStr[:i]+sortedStr[-1]+sortedStr[i+1:-1]+'1'
                break
        # print(sortedStr)
        return sortedStr