def interLeaving(A, B, C):

    # 만약 C[:n] 이 A[:x] 와 B[:y]의 인터리빙이라면 C[n+1:]이 A[x+1:] B[y+1:]의 인터리빙인지의 결과값과 같음

    # base case:
    if not A and not B and not C:
        return True

    elif not C:
        return False

    x = False
    y = False

    if A and C[0] == A[0]:
        x = interLeaving(A[1:], B, C[1:])
    
    if B and C[0] == B[0]:
        y = interLeaving(A, B[1:], C[1:])


    return x or y




def interLeavingDP(A, B, C):
    if len(A) + len(B) != len(C):
        return False

    memo = {} # memo[i, j]는 A 길이 i B 길이 j 까지 인터리빙인지 검사
    memo[0,0] = True

    nA = len(A)
    nB = len(B)

    for i in range(1, nA + 1):
        if memo[(i-1, 0)] and C[i - 1] == A[i - 1]:
            memo[(i, 0)] = True
            
    for j in range(1, nB + 1):
        if memo[(0, j-1)] and C[j - 1] == B[j - 1]:
            memo[(0, j)] = True

    for i in range(1, nA + 1):
        for j in range(1, nB + 1):
            memo[(i, j)] = False
            
            if memo[i-1][j]:
                if A[i-1] == C[i + j -1]:
                    memo[(i, j)] = True

            if memo[i][j-1]:
                if B[j-1] == C[i + j - 1]:
                    memo[(i, j)] = True


    return memo[(nA, nB)]
            
        


