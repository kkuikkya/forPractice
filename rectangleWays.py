def rectangleWays(n, m):
    """ DP를 이용해 구현"""

    # n : 세로, m : 가로

    # memo 0,0 부터 (i, j) 까지 가는 경우의 수
    memo = [[0 for _ in range(m)] for _ in range(n)]


    
    for i in range(0, n):
        memo[i][0] = 1

    for j in range(1, m):
        memo[0][j] = 1

    for i in range(1,n):
        for j in range(1,m):
            memo[i][j] = memo[i-1][j] + memo[i][j-1]

    return memo[n-1][m-1]