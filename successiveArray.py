def successiveSymmetrySubstring(arr):
    """카데인 알고리즘"""

    if(max(arr) <= 0 ):
        return max(arr)
    
    maxSumSoFar = 0
    maxSumEndHere = 0

    for i in range(len(arr)):
        maxSumEndHere += arr[i]

        if maxSumEndHere < 0:
            maxSumEndHere = 0

        if maxSumEndHere > maxSumSoFar:
            maxSumSoFar = maxSumEndHere

    return maxSumSoFar



def successiveSymmetrySubstring2(arr):
    """DP 구현"""

    if(max(arr) <= 0 ):
        return max(arr)

    n = len(arr)
    memoSum = [[0 for _ in range(n)] for _ in range(n)] # i 부터 j 까지의 합

    for i in range(n):
        memoSum[i][i] = arr[i]

    max = 0
    for i in range(n):
        for j in range(n):
            if(j > i):
                memoSum[i][j] = memoSum[i][j-1] + arr[j]
                if(memoSum[i][j] > max):
                    max = memoSum[i][j]
        
    return max


