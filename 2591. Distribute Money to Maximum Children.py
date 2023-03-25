class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money<children:
            return -1
        if money<8 or (money<=8 and children>1):
            return 0

        c = [1 for i in range(children)]
        i = 0
        money = money-children
        while money and i<len(c):
            c[i] += 1
            money -= 1
            if c[i]==8:
                i += 1
            
        print(c)
        cnt = 0
        for i in c:
            if i==8:
                cnt += 1
        
        if money:
            return cnt-1
        if 4 in c and cnt==len(c)-1:
            return cnt-1
        return cnt
            
            
            
        