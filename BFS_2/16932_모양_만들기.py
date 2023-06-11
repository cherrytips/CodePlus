# This code has been copied.
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
group = [[0]*m for _ in range(n)]
group_size = [0]
groupn = 0


def bfs(sx, sy):
  global groupn
  groupn += 1
  q = deque()
  q.append((sx, sy))
  group[sx][sy] = groupn
  cnt = 1
  while q:
    x, y = q.popleft()
    for k in range(4):
      nx, ny = x+dx[k], y+dy[k]
      if 0 <= nx < n and 0 <= ny < m:
        if group[nx][ny] == 0 and a[nx][ny] == 1:
          group[nx][ny] = groupn
          q.append((nx, ny))
          cnt += 1
  group_size.append(cnt)


for i in range(n):
  for j in range(m):
    if a[i][j] == 1 and group[i][j] == 0:
      bfs(i, j)

ans = 0
for i in range(n):
  for j in range(m):
    if a[i][j] == 0:
      near = set()
      for k in range(4):
        nx, ny = i+dx[k], j+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
          if a[nx][ny] == 1:
            near.add(group[nx][ny])
      s = 1
      for neighbor in near:
        s += group_size[neighbor]
      if ans < s:
        ans = s
print(ans)
