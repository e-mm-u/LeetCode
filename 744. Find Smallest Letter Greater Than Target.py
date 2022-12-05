def nextGreatestLetter(letters, target):
    if(target < letters[0]) or (target >= letters[len(letters)-1]):
        return letters[0]
    else:
        return letters[binarySearch(letters, target)]

def binarySearch(letters, target):
    start, end = 0, len(letters)-1
    #  here we will break the loop when start==end
    while(start<end):
        mid = int((start+end)/2)
        # our target is not the index of given target but the value that is grater than target
        # if mid is less than target then we must shift right,
        #  if mid is greater than mid then it is a potential possible answer
        if(letters[mid]<=target):
            start = mid+1
        else:
            end = mid

    return start

# ------------------------------ test cases---------------
# letters = ["c","f","j"] 
# target = "c"
letters = ["c","f","j"] 
target = "a"
# letters = ["x","x","y","y"]
# target = "z"
print(nextGreatestLetter(letters, target))

