import re

# def isPalindrome(s):
#     new_s = re.sub(r'[^a-zA-Z0-9]', "", s)
#     return new_s.lower() == new_s[::-1].lower()

#  using 2 pointers
def isPalindrome(s):
    
    new_s = (re.sub(r'[^a-zA-Z0-9]', "", s)).lower()
    left,right = 0,len(new_s)-1

    while(left<=right):
        if( new_s[left] == new_s[right]):
            left += 1
            right -= 1
            continue
        else:
            return False

    return True

s = "A man, a plan, a canal: Panama"
s = "race a car"
s = " "
print(isPalindrome(s))