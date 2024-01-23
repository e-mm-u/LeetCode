class Solution:
    def maxLength(self, arr: List[str]) -> int: 
        # get rid of any strings with duplicates
        arr = list(filter(lambda s: not any(map(lambda val: val >= 2, Counter(s).values())), arr))
        n = len(arr)

        # check all combinations
        def solve(ind, used):
            if ind == n:
                return 0
            chars = set(list(arr[ind]))
            if chars & used: # intersect
                return solve(ind + 1, used)
            else:
                return max(len(arr[ind]) + solve(ind + 1, used | chars), solve(ind + 1, used))

        return solve(0, set())
