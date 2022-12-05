import math

def findDigits_1(num):
    c = 0
    while(num>0):
        c += 1
        num = int(num/10)
    return c%2==0

    
def findDigits_2(num):
    c = math.log(num)+1
    return c%2 ==0


def findNumbers(nums):
    
    c = 0

    for num in nums :
        if(findDigits_1(num)):
            c += 1
    
    return c

# nums = [12,345,2,6,7896]
nums = [555,901,482,1771]
print(findNumbers(nums))

