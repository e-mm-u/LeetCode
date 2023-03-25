class Solution:
    def evenOddBit(self, n: int) -> List[int]:

        binn = ''
        while n:
            r = n%2
            binn += str(r)
            n //= 2
            
        print(binn)
        even,odd = 0,0
        for i in range(len(binn)):
            if binn[i] == '1':
                
                if i%2==0:
                    even += 1
                else:
                    odd += 1
        #print(even,odd)
        return [even,odd]