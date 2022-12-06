# ----------------------------------------
# Time Complexity	 
# Best	O(n)
# Worst	O(n2)
# Average	O(n2)
# Space Complexity	O(1)
# Stability	Yes
# --------------------------------------------


def insertion_sort(arr):
    for i in range(1, len(arr)):
        
        key = arr[i]
        j = i-1
        # compare each element with the left of it
        while(  j>=0 and key<arr[j]):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

    return arr

arr = [4,63,5,7,8,6,21,4,34,5,7,7]
print(insertion_sort(arr))