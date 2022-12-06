# --------------------------------------------------
# Time Complexity	 
        # Best	O(n2)
        # Worst	O(n2)
        # Average	O(n2)
# Space Complexity	O(1)
# Stability	No
# --------------------------------------------------------
                            # The selection sort is used when

                            # a small list is to be sorted
                            # cost of swapping does not matter
                            # checking of all the elements is compulsory
                            # cost of writing to a memory matters like in flash memory (number of writes/swaps is O(n) as compared to O(n2) of bubble sort)

# --------------------------------------------------------
def selection_sort(arr):
    l = len(arr)
    for i in range(l):
# ------------------- ascending sort ----------------------
        min_index = i
        # as selectiong min, min value will be set in 0 index and we'll then need to sort from 1 to end
        for j in range(i+1,l): 
            if arr[j]<arr[min_index]:
                min_index = j

        # swap 
        arr[i], arr[min_index] = arr[min_index], arr[i]

# ------------------- descending sort ----------------------

        # max_index = i
        # for j in range(i+1,l-i-1):
        #     if( arr[j]> arr[max_index] ):
        #         max_index = j
        # arr[i], arr[max_index] = arr[max_index], arr[i]



    return arr


arr = [4,63,5,7,8,6,21,4,34,5,7,7]
print(selection_sort(arr))