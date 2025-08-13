from collections import deque

moves = [(1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)]

def onBoard(cur):
    return 0 <= cur[0] <= 7 and 0 <= cur[1] <= 7

def tupleSum(a,b):
    return (a[0] + b[0], a[1] + b[1])

def minMove(s, d, moves):
    
    memo = {}
    memo[s] = 0
    
    queue = deque([s])

    while queue:
        current = queue.popleft()

        for move in moves:
            next = tupleSum(current, move)
            
            if onBoard(next):

                if next not in memo:
                    memo[next] = float('inf')
                    
                if memo[next] > memo[current] + 1:
                    memo[next] = memo[current] + 1
                    queue.append(next)

    if d not in memo:
        return None
    
    return memo[d]


