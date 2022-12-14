class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if(digits[-1] != 9):
            digits[-1] += 1
        
        else:
            i = len(digits)-1
            c = False
            while i>=0:
                if(digits[i] != 9):
                    digits[i] += 1
                    c = False
                    i -= 1
                    break
                else :
                    digits[i] = 0
                    c = True
                    i -= 1
                    continue
                
            
            if(c):
                digits.insert(0,1)
                
        return digits