class Solution(object):
    def uniquePaths(self, m, n):

        routematrix = [[0]*m for i in range(n)]
        routematrix[0][0] = 1

        for i in range(1,m):
            routematrix[0][i] = routematrix[0][i-1]
        for j in range(1,n):
            routematrix[j][0] = routematrix[j-1][0]
        for i in range(1,n):
            for j in range(1,m):
                routematrix[i][j] = routematrix[i-1][j] + routematrix[i][j-1]
        return routematrix[n-1][m-1]