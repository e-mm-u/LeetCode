class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        n = len(arr)
        res, stack = 0, []

        for i in range(n+1):
            while stack and (i==n or arr[stack[-1]]>arr[i]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                right = i

                cnt = (mid-left)*(right-mid)
                res += cnt*arr[mid]

            stack.append(i)
        return res%mod
