def symmertrySubstring(s : str):

    strlen = len(s)

    maxlen = 0

    for i in range(strlen): # 배열의 시작과 끝을 생각하자......
        memo[i][i] = int(s[i])

    for length in range(2, strlen + 1): # len 은 부분 문자열 길이

        for i in range(0, strlen - length + 1): # i는 시작 인덱스

            j = i + length - 1
            k = length // 2

            memo[i][j] = memo[i][i + k - 1] + memo[i + k][j]

            if (memo[i][i + k - 1] == memo[i + k][j] and length % 2 == 0):
                maxlen = length

    return maxlen


memo = [[0 for _ in range(4)] for _ in range(4)]
    
    
    


