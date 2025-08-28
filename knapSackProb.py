from collections import deque

def knapSackProb(weight, value, rest, idx = 0):
    """ 0-1 KnapSack Problem """

    # base case: 가방에 남은 공간이 없는 경우
    if rest <= 0 or idx > len(weight) - 1:
        return 0

    contained = 0
    if rest >= weight[idx]:
        contained = knapSackProb(weight, value, rest - weight[idx], idx + 1) +  value[idx]

    uncontained = knapSackProb(weight, value, rest, idx + 1)

    return max(contained, uncontained)


def knapSackProbDP(weight, value, rest):

    maxValue = {} # maxValue[(i,j)] 는 i 의 가방공간에 j 번쨰 아이템까지 사용했을 때 최대 value
    maxValue[(0,0)] = 0

    # 가방의 공간이 없는 경우 아이템을 아무리 추가해도 value 는 0
    for j in range(1, len(weight) + 1):
        maxValue[(0, j)] = 0

    # 추가할 아이템이 없는 경우 아무리 가방 무게를 줘도 value는 0 
    for i in range(1, rest + 1):
        maxValue[(i, 0)] = 0

    for i in range(1, rest + 1):
        for j in range(1, len(weight) + 1):

            # j번째 아이템을 추가하지 않는 경우
            uncontained = maxValue[(i, j-1)]

            # j번째 아이템을 추가하는 경우
            contained = 0
            if i >= weight[j-1]:
                contained = maxValue[(i- weight[j-1], j-1)] + value[j-1]

            maxValue[(i,j)] = max(contained, uncontained)
    
    return maxValue[(rest, len(weight))]


def knapSackProbPrint(weight, value, rest):

    maxValue = {} # maxValue[(i,j)] 는 i 의 가방공간에 j 번쨰 아이템까지 사용했을 때 최대 value
    maxValue[(0,0)] = 0

    # 가방의 공간이 없는 경우 아이템을 아무리 추가해도 value 는 0
    for j in range(1, len(weight) + 1):
        maxValue[(0, j)] = 0

    # 추가할 아이템이 없는 경우 아무리 가방 무게를 줘도 value는 0 
    for i in range(1, rest + 1):
        maxValue[(i, 0)] = 0

    for i in range(1, rest + 1):
        for j in range(1, len(weight) + 1):

            # j번째 아이템을 추가하지 않는 경우
            uncontained = maxValue[(i, j-1)]

            # j번째 아이템을 추가하는 경우
            contained = 0
            if i >= weight[j-1]:
                contained = maxValue[(i- weight[j-1], j-1)] + value[j-1]

            maxValue[(i,j)] = max(contained, uncontained)


    #BFS
    queue = deque()
    queue.append((rest, len(weight), []))
    result = []

    while queue:
        currenti, currentj, currentlist = queue.popleft()

        if currentj == 0:
            tmp = sorted(currentlist)
            if tmp not in result:
                result.append(tmp)
            continue

        # 미포함 하는 경우
        if maxValue[(currenti, currentj)] == maxValue[(currenti, currentj - 1)]:
            queue.append((currenti, currentj-1, currentlist))

        # 포함하는 경우
        if currenti >= weight[currentj -1] and maxValue[(currenti, currentj)] == maxValue[(currenti - weight[currentj - 1], currentj-1)] + value[currentj-1]:
            queue.append((currenti - weight[currentj -1], currentj -1, currentlist + [currentj-1]))

        
    print(result, "BFS")
    
    return maxValue[(rest, len(weight))]

weight = [2, 3, 4, 5]
value = [3, 4, 5, 6]
rest = 5

knapSackProbPrint(weight, value, rest)