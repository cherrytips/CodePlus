# This code has been copied.
from collections import deque
moves = list(zip([0, 0, 1, 1, 2, 2], [1, 2, 0, 2, 0, 1]))
ans = [False]*201
check = [[False]*201 for _ in range(201)]
cap = list(map(int, input().split()))
sum = cap[2]
q = deque()
q.append((0, 0))
check[0][0] = True
ans[cap[2]] = True
while q:
  now = q.popleft()
  cur = [now[0], now[1], sum-now[0]-now[1]]
  for f, t in moves:
    next = cur[:]
    next[t] += next[f]
    next[f] = 0
    if next[t] >= cap[t]:
      next[f] = next[t] - cap[t]
      next[t] = cap[t]
    if not check[next[0]][next[1]]:
      check[next[0]][next[1]] = True
      q.append((next[0], next[1]))
      if next[0] == 0:
        ans[next[2]] = True
for i in range(0, cap[2]+1):
  if ans[i]:
    print(i, end=' ')
print()
