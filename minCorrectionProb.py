def minCorrectionProb(str1, str2):

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

        removeCost = minCorrectionProb(str1[:-1], str2)

        replaceCost = minCorrectionProb(str1[:-1], str2[:-1])

        return 1 + min(insertCost, removeCost, replaceCost)