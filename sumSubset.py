def sumSubset(setList, X, memo):
    """하향식 재귀 호출로 해결"""

    #base case
    if X == 0:
        return True

    if not setList:
        return False
    
    p = setList[0]
    remainList = setList[1:]

    return sumSubset(remainList, X-p) or sumSubset(remainList, X)


print(sumSubset([1,2,3,6],9))

def sumSubsetDP(setList,X):

    memo = {} # memo[(i,j)] 원소 i 개로 합 j 를 만들수 있는가? (j <= X)

    memo[(0,0)] = True

    n = len(setList)

    for i in range(1, n + 1):
        memo[(i, 0)] = True


    for j in range(1, X + 1):
        memo[(0, j)] = False

    for i in range(1,n+1):
        num = setList[i-1] # 현재 보고 있는 숫자

        for j in range(1,X+1):
            
            include = False
            if j >= num:
                include = memo[(i-1, j-num)]

            exclude = memo[(i-1, j)]


            memo[(i,j)] = include or exclude

    return memo[(n, X)]
