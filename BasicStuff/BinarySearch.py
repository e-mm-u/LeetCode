# ____________________________________
# _______ time complexity _________________\
    # Best case : O(1)
    # Avg case : O(log n)
    # Worst case : O(log n)
# -------------------------------------------------------------
    # space complexity : O(1)
# ................................................................
#___________________________________________
#_________ IETARATIVE METHOD _______________\

def binarySearch(array, target):
    start, end = 0, len(array)-1

    while(start<=end):
        mid = start + (end-start)//2

        if(array[mid]==target):
            return mid

        elif(array[mid]<target):
            start = mid+1

        else:
            end = mid-1
        
    return -1

# __________________________________________________
# ____________________ RECURSIVE METHOD ______________\

def binarySearch(array, target, start, end):

    if(end>=start):
        mid = start + (end-start)//2

        if(array[mid]==target):
            return mid
        
        elif(array[mid]<target):
            return binarySearch(array, target, mid+1, end)
        
        else:
            return binarySearch(array, target, start, mid-1)
    
    else:
        return -1