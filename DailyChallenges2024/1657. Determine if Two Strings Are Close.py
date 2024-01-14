class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1)!=set(word2):
            return False
        
        w1, w2 = {}, {}
        for i in range(len(word1)):
            w1[word1[i]] = w1.get(word1[i],0)+1
            w2[word2[i]] = w2.get(word2[i],0)+1
        
        return sorted(w1.values())==sorted(w2.values())