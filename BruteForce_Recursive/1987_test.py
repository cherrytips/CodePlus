# import sys
# readline = sys.stdin.readline

# R, C = map(int, readline().split())
# board = [readline().strip() for _ in range(R)]
# check = [False]*26
# check[ord(board[0][0])-ord('A')] = True

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]


# def go(board, check, x, y):
#   ans = 0
#   for k in range(4):
#     nx, ny = x+dx[k], y+dy[k]
#     if 0 <= ny < R and 0 <= nx < C:
#       ch = ord(board[ny][nx])-ord('A')
#       if check[ch] == False:
#         check[ch] = True
#         temp = go(board, check, nx, ny)
#         if ans < temp:
#           ans = temp
#         check[ch] = False
#   return ans+1


# print(go(board, check, 0, 0))

# 첫 번째 칸은 무조건 지남 => 시작 index = 0, 0
# dy,dx 를 상,하,좌,우 로 놓고 for 문 돌려서 모든 칸 방문
# check 배열 = False, True 판별 => 0 부터 25 : A ~ Z
# 있으면 => 답과 비교하여 max 구하기

# 이동 횟수도 다음 recursive 로 전달 (초기 이동횟수 = 1)
# recursive 포함된 for 문 끝나면 check 배열에서 현재 알파벳 False 복귀

import sys
readline = sys.stdin.readline

R, C = map(int, readline().split())
board = []
check = [False for _ in range(26)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 0

for _ in range(R):
  board.append(readline().strip())


def move(y, x, check, cnt):
  global ans

  if check[ord(board[y][x])-65] == True:
    ans = max(ans, cnt-1)
    return

  check[ord(board[y][x])-65] = True

  for i in range(4):
    ny, nx = y+dy[i], x+dx[i]
    if 0 <= ny < R and 0 <= nx < C:
      move(ny, nx, check, cnt+1)

  check[ord(board[y][x])-65] = False

  return


move(0, 0, check, 1)
print(ans)
