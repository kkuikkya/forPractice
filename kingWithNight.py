from collections import deque

def solve_with_tabulation_dp(s, d):
    """
    타뷸레이션(Bottom-Up) DP 방식으로 '마왕' 문제 풀기
    (BFS 알고리즘을 DP 관점에서 해석)
    """
    sx, sy = s
    dx, dy = d

    if (sx, sy) == (dx, dy):
        return 0

    # 1. DP 테이블 준비
    # dp_table[r][c] := 시작점에서 (r, c)까지 가는 데 필요한 최소 이동 횟수
    # -1은 아직 계산되지 않음(방문하지 않음)을 의미
    dp_table = [[-1 for _ in range(8)] for _ in range(8)]

    # 이동 규칙 정의
    all_moves = [
        (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1), # 왕
        (-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(1,-2),(-1,2),(1,2)  # 나이트
    ]

    # 2. 가장 작은 문제의 답을 테이블에 기록
    # 시작점 (가장 작은 문제)은 0번만에 갈 수 있음
    dp_table[sx][sy] = 0
    
    # 계산할 문제들을 순서대로 담아둘 큐(Queue) 준비
    queue = deque([(sx, sy)])

    # 3. 반복문을 통해 DP 테이블을 채워나감 (Bottom-Up)
    while queue:
        # 현재 계산할 위치(문제)를 꺼냄
        current_x, current_y = queue.popleft()

        # 현재 위치의 답(최소 이동 횟수)을 가져옴
        current_moves = dp_table[current_x][current_y]

        # 16가지 이동 규칙을 적용해 다음 문제들을 풀어 테이블을 채움
        for dx_move, dy_move in all_moves:
            next_x, next_y = current_x + dx_move, current_y + dy_move

            # 테이블 범위 안에 있고, 아직 풀리지 않은 문제라면 (방문한 적 없다면)
            if 0 <= next_x < 8 and 0 <= next_y < 8 and dp_table[next_x][next_y] == -1:
                # 다음 문제의 답을 테이블에 기록
                dp_table[next_x][next_y] = current_moves + 1
                
                # 목적지에 도달했다면 바로 답을 반환
                if (next_x, next_y) == (dx, dy):
                    return dp_table[next_x][next_y]
                
                # 다음 차례에 계산할 문제라고 큐에 추가
                queue.append((next_x, next_y))
    
    return -1 # 모든 경로를 탐색해도 도착하지 못한 경우

# --- 실행 ---
start_pos = (0, 0)
end_pos = (7, 7)
min_moves = solve_with_tabulation_dp(start_pos, end_pos)
print(f"타뷸레이션 DP 결과: {min_moves}번")


def find_minimum_moves(s, d):
    """마왕(왕+나이트)이 S에서 D까지 가는 최소 이동 횟수를 BFS로 찾습니다."""

    # 1. 초기 설정
    sx, sy = s
    dx, dy = d

    if (sx, sy) == (d, dy):
        return 0

    # 2. 이동 규칙 정의: 왕(8방향)과 나이트(8방향)의 움직임을 모두 합칩니다.
    all_moves = [
        # 왕의 움직임
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1),
        # 나이트의 움직임
        (-2, -1), (-2, 1),
        (2, -1), (2, 1),
        (-1, -2), (1, -2),
        (-1, 2), (1, 2)
    ]

    # 3. BFS 준비
    # 큐(Queue)에는 (x좌표, y좌표, 현재까지의 이동 횟수)를 저장합니다.
    queue = deque([(sx, sy, 0)])
    
    # 방문한 위치를 기록해 무한 루프를 방지합니다.
    visited = set([(sx, sy)])

    # 4. BFS 루프 시작
    while queue:
        # 큐의 가장 앞에서 데이터(현재 위치, 이동 횟수)를 꺼냅니다.
        current_x, current_y, moves = queue.popleft()

        # 5. 모든 가능한 다음 수를 탐색합니다. (여기가 질문하신 '루프' 부분입니다)
        for dx_move, dy_move in all_moves:
            next_x, next_y = current_x + dx_move, current_y + dy_move

            # 목적지에 도착했다면, 현재까지의 이동 횟수에 1을 더해 반환합니다.
            if (next_x, next_y) == (dx, dy):
                return moves + 1

            # 체스판 범위(0~7) 안에 있고, 아직 방문하지 않은 곳인지 확인합니다.
            if 0 <= next_x < 8 and 0 <= next_y < 8 and (next_x, next_y) not in visited:
                visited.add((next_x, next_y)) # 방문했다고 표시
                queue.append((next_x, next_y, moves + 1)) # 큐에 다음 탐색 지점을 추가

    return -1 # 큐가 비었는데도 도착하지 못했다면 경로가 없는 경우입니다.

# --- 예제 실행 ---
start_pos = (0, 0)
end_pos = (7, 7)
min_moves = find_minimum_moves(start_pos, end_pos)

print(f"({start_pos[0]}, {start_pos[1]})에서 ({end_pos[0]}, {end_pos[1]})까지의 최소 이동 횟수: {min_moves}번")


def find_minimum_moves2(s, d, visited):
    """마왕(왕+나이트)이 S에서 D까지 가는 최소 이동 횟수를 BFS로 찾습니다."""

    # 1. 초기 설정
    sx, sy = s
    dx, dy = d

    #base case

    if(s == d):
        return 0

    if(s in visited):
        return float('inf')
    
    visited.add(s)

    # 2. 이동 규칙 정의: 왕(8방향)과 나이트(8방향)의 움직임을 모두 합칩니다.
    all_moves = [
        # 왕의 움직임
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1),
        # 나이트의 움직임
        (-2, -1), (-2, 1),
        (2, -1), (2, 1),
        (-1, -2), (1, -2),
        (-1, 2), (1, 2)
    ]


    able_moves = []

    for (i,j) in all_moves:
        if 0 <= sx + i < 8 and 0 <= sy + j < 8 and (sx +i, sy + j) not in visited:
            able_moves.append((i , j))

    if not able_moves: # 더 이상 갈 곳이 없는 막다른 길이라면
        visited.remove(s) # ★ 중요: 실패 시에도 방문 기록은 삭제해야 함
        return float('inf') # 이 경로는 '실패(무한대)'라고 보고

    min_cost = 1 + min(find_minimum_moves2((sx + i, sy + j), d, visited) for i, j in able_moves)

    visited.remove(s) # 백트래킹 끝

    return min_cost


visited = set()

# ㅅㅂ 존나 어렵네