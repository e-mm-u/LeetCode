# _______________________________________ 
#_ _________Time Complexity	__________-- 
    # Best	O(n)
    # Worst	O(n^2)
    # Average	O(n^2)
    # Space Complexity	O(1)
    # Stability	Yes
# -------------------------------
            # Bubble sort is used if

            # complexity does not matter
            # short and simple code is preferred
# --------------------------------------------------

def bubble_sort(arr):
    for i in range( len(arr) ):
        swapped = False
        for j in range( len(arr)-i-1):

            #  compare two adjacent elements
            if(arr[j] > arr[j+1]):
                # swap
                temp = arr[j+1]
                arr[j+1] = arr[j] 
                arr[j] = temp

                swapped = True

        if not swapped : # already sorted
            break
                
    return arr

arr = [4,63,5,7,8,6,21,4,34,5,7,7]
print(bubble_sort(arr))