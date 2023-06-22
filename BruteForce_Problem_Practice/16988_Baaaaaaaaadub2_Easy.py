# This code has been copied.
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def bfs():
  ans = 0
  check = [[False]*m for _ in range(n)]
  for i in range(n):
    for j in range(m):
      if a[i][j] == 2 and check[i][j] == False:
        dead = True
        q = deque()
        q.append((i, j))
        check[i][j] = True
        cur = 0
        while q:
          cur += 1
          x, y = q.popleft()
          for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
              if a[nx][ny] == 0:
                dead = False
              elif a[nx][ny] == 2 and check[nx][ny] == False:
                q.append((nx, ny))
                check[nx][ny] = True
        if dead:
          ans += cur
  return ans


for x1 in range(n):
  for y1 in range(m):
    if a[x1][y1] != 0:
      continue
    for x2 in range(n):
      for y2 in range(m):
        if x1 == x2 and y1 == y2:
          continue
        if a[x2][y2] != 0:
          continue
        a[x1][y1] = 1
        a[x2][y2] = 1
        cur = bfs()
        if ans < cur:
          ans = cur
        a[x1][y1] = 0
        a[x2][y2] = 0
print(ans)
