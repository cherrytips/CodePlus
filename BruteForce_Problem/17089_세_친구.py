# This code has been copied.
#!/usr/bin/python3
n, m = map(int, input().split())
a = [[False]*(n+1) for _ in range(n+1)]
degree = [0] * (n+1)
for _ in range(m):
  x, y = map(int, input().split())
  a[x][y] = a[y][x] = True
  degree[x] += 1
  degree[y] += 1

ans = -1

for i in range(1, n+1):
  for j in range(1, n+1):
    if a[i][j]:
      for k in range(1, n+1):
        if a[i][k] and a[j][k]:
          s = degree[i] + degree[j] + degree[k] - 6
          if ans == -1 or ans > s:
            ans = s

print(ans)
