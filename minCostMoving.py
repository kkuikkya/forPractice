def minCostMoving1(cost, m: int, n: int):
    """메모전략을 이용해서 구현 시간복잡도 O(n^2)"""

    if(memo[m][n] != 0):
        return memo[m][n]


    if ( m == 0 and n == 0):
        memo[m][n] = cost[0][0]
    
    elif (m == 0):
        memo[m][n] = minCostMoving1(cost, 0 , n-1) + cost[0][n]
    
    elif (n == 0):
        memo[m][n] = minCostMoving1(cost, m-1, 0) + cost[m][0]

    else:
        x = minCostMoving1(cost, m-1, n)
        y = minCostMoving1(cost, m, n-1)
        memo[m][n] = min(x,y) + cost[m][n]

    return memo[m][n]

def minCostMoving2(cost):
    """DP를 이용해 구현"""

    memo[0][0] = cost[0][0]

    for j in range(1, len(cost[0])):
        memo[0][j] = memo[0][j - 1] + cost[0][j]

    for i in range(1, len(cost)):
        memo[i][0] = memo[i - 1][0] + cost[i][0]

    for i in range(1, len(cost)):
        for j in range(1, len(cost[0])):
            memo[i][j] = min(memo[i-1][j], memo[i][j-1]) + cost[i][j]

    return memo[len(cost) - 1][len(cost[0]) - 1]




memo= [[0 for _ in range(3)] for _ in range(4)]

