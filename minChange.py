from collections import deque

def minChange(coin, rest, idx = 0):

    # base case
    if rest == 0:
        return 0

    if idx >= len(coin) or rest < 0:
        return float("inf")

    containUsed = float("inf")
    uncontained = float("inf")

    if rest - coin[idx] >= 0: # 포함하는 경우
        containUsed = 1 + minChange(coin, rest - coin[idx], idx)
        
    # 현재 코인을 미포함하는 경우
    uncontained = minChange(coin, rest, idx + 1)

    return min(containUsed, uncontained)

def minChangeDP(coin, rest):
    
    # memo[i] 는 i 원을 만드는데 필요한 동전 개수
    memo = [rest + 1] * (rest + 1)

    memo[0] = 0

    for i in range(1, rest + 1):

        for j in range(len(coin)):

            if coin[j] <= i:
                temp = memo[i - coin[j]]

                if temp != rest + 1 and temp + 1 < memo[i]:
                    memo[i] = temp + 1


    return memo[rest]
    

def minChangePrint(coin, rest):
    
    # memo[i] 는 i 원을 만드는데 필요한 동전 개수
    memo = [rest + 1] * (rest + 1)

    memo[0] = 0

    for i in range(1, rest + 1):

        for j in range(len(coin)):

            if coin[j] <= i:
                temp = memo[i - coin[j]]

                if temp != rest + 1 and temp + 1 < memo[i]:
                    memo[i] = temp + 1

    if memo[rest] == rest + 1:
        print("경우의 수 없음")
        return None

    queue = deque()
    queue.append((rest, []))

    result = []

    while queue:
        s, selected = queue.popleft()

        if s == 0:
            result.append(sorted(selected))

        for i in range(len(coin)):
            if s >= coin[i] and memo[s- coin[i]] == memo[s] - 1:
                queue.append((s- coin[i], selected + [coin[i]]))


    uniqueResult = set(tuple(item) for item in result)
    result = [list(item) for item in uniqueResult]

    print(result)
        
        
    return memo[rest]




print(minChangePrint([50, 20, 10, 5, 2, 1], 65))