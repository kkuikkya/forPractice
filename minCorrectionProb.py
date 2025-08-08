def minCorrectionProb(str1, str2):
    """재귀를 이용한 풀이"""

    # base case 어느 한쪽의 길이가 0이라면 삽입 or 삭제의 연산이 n번 필요
    if len(str1) == 0:
        return len(str2)

    if len(str2) == 0:
        return len(str1)

    # 최적의 하위 구조 & 분할정복 -> 맨 끝이 다른 경우, 같은 경우로 나누고 다른 경우 추가, 제거, 대체를 시행하고 횟수 추가

    if(str1[-1] == str2[-1]):
        return minCorrectionProb(str1[:-1], str2[:-1])
    
    else:
        insertCost = minCorrectionProb(str1, str2[:-1])

        replaceCost = minCorrectionProb(str1[:-1], str2[:-1])

        removeCost = minCorrectionProb(str1[:-1], str2)

        return 1 + min(insertCost, replaceCost, removeCost)



def minCorrectionProb2(str1, str2):
    """DP를 이용한 풀이"""

    n1 = len(str1)
    n2 = len(str2)

    memo = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]


    for i in range(1, n1 + 1):
        memo[i][0] = i
    
    for j in range(1, n2 + 1):
        memo[0][j] = j

    # memo[i][j] str1의 [i - 1] 와 str2 [j - 1] 까지 비교함(i 와 j 의 길이까지 비교)
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if(str1[i-1] == str2[j-1]):
                memo[i][j] = memo[i-1][j-1] 

            else:
                y = memo[i][j-1] # insert
                x = memo[i-1][j-1] # replace
                z = memo[i-1][j] # remove

                memo[i][j] = 1 + min(x,y,z)

    return memo[n1][n2]
