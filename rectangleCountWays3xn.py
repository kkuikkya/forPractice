def countWays(n):
    if n <= 1 or n % 2 != 0:
        return 0

    elif n == 2:
        return 3

    if(memo[n] != -1):
        return memo[n]

    ways = 0

    for i in range(4, n+1, 2):
        ways +=  2*countWays(n - i)

    ways += 3*countWays(n-2)

    memo[n] = ways

    return ways


memo = [0 for _ in range(5)]