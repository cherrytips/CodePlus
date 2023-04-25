# This code has been copied.
import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
board = list(readline().strip() for _ in range(N))
dy = [-1, 1, 0, 0]  # 상하좌우
dx = [0, 0, -1, 1]
y1 = x1 = y2 = x2 = -1

for i in range(N):
  for j in range(M):
    if board[i][j] == 'o':
      if y1 == -1:
        y1, x1 = i, j
      else:
        y2, x2 = i, j


def press(y1, x1, y2, x2, cnt):
  fall1 = False
  fall2 = False
  if cnt > 10:
    return -1
  if y1 < 0 or N <= y1 or x1 < 0 or M <= x1:
    fall1 = True
  if y2 < 0 or N <= y2 or x2 < 0 or M <= x2:
    fall2 = True
  if fall1 and fall2:
    return -1
  if fall1 or fall2:
    return cnt

  ans = -1
  for i in range(4):
    ny1, nx1, ny2, nx2 = y1+dy[i], x1+dx[i], y2+dy[i], x2+dx[i]
    if 0 <= ny1 < N and 0 <= nx1 < M and board[ny1][nx1] == '#':
      ny1, nx1 = y1, x1
    if 0 <= ny2 < N and 0 <= nx2 < M and board[ny2][nx2] == '#':
      ny2, nx2 = y2, x2
    temp = press(ny1, nx1, ny2, nx2, cnt+1)
    if temp == -1:
      continue
    if ans == -1 or ans > temp:
      ans = temp

  return ans


print(press(y1, x1, y2, x2, 0))
