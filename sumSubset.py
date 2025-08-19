from collections import deque

def sumSubset(setList, X):
    """하향식 재귀 호출로 해결"""

    #base case
    if X == 0:
        return True

    if not setList:
        return False
    
    p = setList[0]
    remainList = setList[1:]

    return sumSubset(remainList, X-p) or sumSubset(remainList, X)


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



def sumSubsetDPPrint(setList,X):
    """배열 출력하기"""

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


    result = []
    
    # 백트래킹 DFS
    def findAll(i, j, current_subset):
        if j == 0:
            result.append(current_subset)
            return

        if i == 0:
            return
        
        num = setList[i-1]

        # exclude
        if memo.get((i - 1, j), False):
            findAll(i - 1, j, current_subset)

        # include
        if j >= num and memo.get((i - 1, j - num), False):
            findAll(i - 1, j - num, [num] + current_subset)

    findAll(n, X, [])

    print(result)

    return memo[(n, X)]




def onlyTwoForX(setList, X):
    """연습문제 5-7"""

# 1. 일단 정렬
# 2. 원소 선택
# 3. 남은 원소들 중 가운데 값을 X와 비교
# 4. 반복..

    tmplist = sorted(setList)

    n = len(tmplist)
    
    for i in range(n):
        num1 = tmplist[i]

        left = i + 1
        right = n-1

        while left <= right:
            mid = (left + right) // 2

            if num1 + tmplist[mid] < X:
                left = mid + 1
        
            elif num1 + tmplist[mid] > X:
                right = mid - 1

            else:
                return True
    
    return False
        


sumSubsetDPPrint([1,2,3,6], 6)