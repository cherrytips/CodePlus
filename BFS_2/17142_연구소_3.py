# This code has been copied.
from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
candi = []
ans = -1
for i in range(n):
  for j in range(n):
    if a[i][j] == 2:
      # 차이 1 (연구소 2는 a[i][j] = 0; 이 적혀있음)
      candi.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
  d = [[-1]*n for _ in range(n)]
  q = deque()
  for i in range(n):
    for j in range(n):
      if a[i][j] == 3:
        q.append((i, j))
        d[i][j] = 0
  while q:
    x, y = q.popleft()
    for k in range(4):
      nx = x+dx[k]
      ny = y+dy[k]
      if 0 <= nx < n and 0 <= ny < n:
        if a[nx][ny] != 1 and d[nx][ny] == -1:
          d[nx][ny] = d[x][y] + 1
          q.append((nx, ny))
  cur = 0
  for i in range(n):
    for j in range(n):
      if a[i][j] == 0:  # 차이 3
        if d[i][j] == -1:
          return
        if cur < d[i][j]:
          cur = d[i][j]
  global ans
  if ans == -1 or ans > cur:
    ans = cur


def go(index, cnt):
  if index == len(candi):
    if cnt == m:
      bfs()
  else:
    x, y = candi[index]
    a[x][y] = 3
    go(index+1, cnt+1)
    a[x][y] = 2  # 차이 2
    go(index+1, cnt)


go(0, 0)
print(ans)
