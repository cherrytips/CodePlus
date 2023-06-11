# This code has been copied.
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
a = [input() for _ in range(n)]
water = [[-1]*m for _ in range(n)]
dist = [[-1]*m for _ in range(n)]
q = deque()
for i in range(n):
  for j in range(m):
    if a[i][j] == '*':
      q.append((i, j))
      water[i][j] = 0
    elif a[i][j] == 'S':
      sx, sy = i, j
    elif a[i][j] == 'D':
      ex, ey = i, j
while q:
  x, y = q.popleft()
  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if 0 <= nx < n and 0 <= ny < m:
      if water[nx][ny] != -1:
        continue
      if a[nx][ny] in 'XD':
        continue
      water[nx][ny] = water[x][y] + 1
      q.append((nx, ny))

q.append((sx, sy))
dist[sx][sy] = 0
while q:
  x, y = q.popleft()
  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if 0 <= nx < n and 0 <= ny < m:
      if dist[nx][ny] != -1:
        continue
      if a[nx][ny] == 'X':
        continue
      if water[nx][ny] != -1 and dist[x][y]+1 >= water[nx][ny]:
        continue
      dist[nx][ny] = dist[x][y]+1
      q.append((nx, ny))

if dist[ex][ey] == -1:
  print('KAKTUS')
else:
  print(dist[ex][ey])
