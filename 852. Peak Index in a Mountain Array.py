class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def binarySearch(arr):
            start, end = 0, len(arr)-1
            while(start<end):
                # print("start : ", start, "end :", end)
                mid = int((start+end)/2)
                # print('mid', mid)

                # if nums[mid] < nums[mid+1] -> increasing order
                if(arr[mid]<arr[mid+1]):
                    # print('increasing part')
                    start = mid + 1
                    # print('start ', start)

                # if nums[mid] > nums[mid+1] -> decreasing order
                else:
                    # print('decreasing part')
                    end = mid
                    # print('end ', end)

            return start
        return binarySearch(arr)