class Solution:
    def categorizeBox(length, width, height, mass):
        heavy = mass>= 100
        bulky = False
        
        if(length>=10000 or width>=10000 or height>=10000):
            bulky = True
        else:
            if(length*width*height>=1000000000):
                bulky = True
        
        if(bulky and heavy):
            return "Both"
        elif(bulky):
            return "Bulky"
        elif(heavy):
            return "Heavy"
        else:
            return "Neither"
            