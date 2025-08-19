def longestCommonSubsequence(X, Y):

    # base case
    if not X or not Y:
        return 0

    result = 0

    if X[0] == Y[0]:
        result += 1
        return result + longestCommonSubsequence(X[1:], Y[1:])

    else:
        removex = longestCommonSubsequence(X[1:], Y)
        removey = longestCommonSubsequence(X, Y[1:])
        return result + max(removex, removey)


def longestCommonSubsequenceDP(X,Y):

    nX = len(X)
    nY = len(Y)

    memo = {}
    for i in range(nX+1):
        memo[(i, 0)] = 0
        
    for j in range(1, nY+1):
        memo[(0, j)] = 0

    for i in range(1, nX+1):
        for j in range(1, nY+1):
            if X[i-1] == Y[j-1]:   
                memo[(i,j)] = memo[(i-1, j-1)] + 1

            else:
                memo[(i,j)] = max(memo[(i-1, j)], memo[(i, j-1)])

    return memo[(nX, nY)]


print(longestCommonSubsequence("AACEDEF", "AOOEDCF"))
print(longestCommonSubsequenceDP("AACEDEF", "AOOEDCF"))