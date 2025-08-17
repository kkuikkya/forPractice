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

def allOfInterleavings(A, B):
    """
    두 문자열의 모든 인터리빙 조합을 중복없이 반환하는 함수
    """
    results = []

    def solve(rem_a, rem_b, current_str):
        """A 와 B 둘중에 무엇을 추가할지 선택해야됨. 이렇게 해도 되는이유는 맨 첫글자를 하나씩 뽑아서 쓰면
        절대 순서가 섞일 일이 없기 떄문임"""


        if not rem_a and not rem_b:
            results.append(current_str)
            return

        if rem_a:
            solve(rem_a[1:], rem_b, current_str + rem_a[0])

        if rem_b:
            solve(rem_a, rem_b[1:], current_str + rem_b[0])

    solve(A, B, "")
    
    # 중복된 경우의 제거를 위해 세트로 바꿨다가 다시 리스트
    return list(set(results))

def allOfInterleavingsDP(A, B):

    memo = {} # memo[(i,j)] 는 길이 i와 j 까지 인터리빙을 만듦
    memo[(0,0)] = [""]

    nA = len(A)
    nB = len(B)

    # base case A, B의 길이가 0 인경우
    for i in range(1, nA + 1):
        memo[(i,0)] = [A[:i]]

    for j in range(1, nB + 1):
        memo[(0,j)] = [B[:j]]

    for i in range(1, nA + 1):
        for j in range(1, nB + 1):
            memo[(i,j)] = [x + A[i-1]for x in memo[(i-1,j)]] + [y + B[j-1] for y in memo[(i, j-1)]]

    return memo[(nA,nB)]
    