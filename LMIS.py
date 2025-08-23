def LMIS(arr):
    """실패한 코드... 카데인 알고리즘을 떠올리며 작성했지만 [3, 5, 2, 6] 등 [2]로 초기화 하는 과정에서 더 좋은 미래를 잃어버림
     책에 나와있는 예제에만 너무 집중한.. 왜 이 반례를 생각 못했을까 아쉽네"""

    lmis = []
    lmis.append(arr.pop(0)) # 첫번째 원소

    maxlen = 1
    curlen = 1


    while arr: 

        current = arr.pop(0)

        print(lmis, curlen, maxlen)

        if current >= lmis[len(lmis) - 1]:
            curlen += 1
            lmis.append(current)

            if maxlen < curlen:
                maxlen = curlen

        else:
            for i in range(len(lmis) - 1, -1, -1):
                if lmis[i] < current:
                    lmis = lmis[:i + 1] + [current]
                    curlen = len(lmis)
                    break

            else:
                lmis = [current]
                curlen = len(lmis)

    return maxlen



def LMIS2(arr):

    memo = [1 for _ in range(len(arr))] # memo[i] 는 i 번쨰 원소로 끝나는 LMS

    for i in range(len(arr)):
        for j in range(i):
            if arr[j] <= arr[i] and memo[j] + 1 >= memo[i]:
                memo[i] = memo[j] + 1
    
    maxVal = max(memo)
    maxidx = memo.index(maxVal)
    result = [arr[maxidx]]
    recent = maxidx

    for i in range(maxidx ,-1, -1):
        if arr[i] <= arr[recent] and memo[i] == memo[recent] - 1:
            result = [arr[i]] + result
            recent = i

    print(result)

    return max(memo)

    
print(LMIS2([7,1,5,4,2,4,9]))

    



            







