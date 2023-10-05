class Solution(object):
    def climbStairs(self, n):
        if n==1:
            return 1
        arr = [0]*(n+2)
        arr[n] = 1
        arr[n-1] = 1
        for i in range(n-2,-1,-1):
            arr[i] = arr[i+1] + arr[i+2]
        return arr[0]