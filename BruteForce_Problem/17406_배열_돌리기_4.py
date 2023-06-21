# This code has been copied.
#!/usr/bin/python3
from copy import deepcopy


def next_permutation(a):
  i = len(a)-1
  while i > 0 and a[i-1] >= a[i]:
    i -= 1
  if i <= 0:
    return False
  j = len(a)-1
  while a[j] <= a[i-1]:
    j -= 1

  a[i-1], a[j] = a[j], a[i-1]

  j = len(a)-1
  while i < j:
    a[i], a[j] = a[j], a[i]
    i += 1
    j -= 1

  return True


def go(a, t):
  row, col, size = t
  groups = []
  for s in range(1, size+1):
    group = []
    # (r-s, c-s) -> (r-s, c+s)
    for c in range(col-s, col+s):
      group.append(a[row-s][c])
    # (r-s, c+s) -> (r+s, c+s)
    for r in range(row-s, row+s):
      group.append(a[r][col+s])
    # (r+s, c+s) -> (r+s, c-s)
    for c in range(col+s, col-s, -1):
      group.append(a[row+s][c])
    # (r+s, c-s) -> (r-s, c-s)
    for r in range(row+s, row-s, -1):
      group.append(a[r][col-s])
    groups.append(group)
  for s in range(1, size+1):
    group = groups[s-1]
    group = group[-1:] + group[:-1]
    index = 0
    # (r-s, c-s) -> (r-s, c+s)
    for c in range(col-s, col+s):
      a[row-s][c] = group[index]
      index += 1
    # (r-s, c+s) -> (r+s, c+s)
    for r in range(row-s, row+s):
      a[r][col+s] = group[index]
      index += 1
    # (r+s, c+s) -> (r+s, c-s)
    for c in range(col+s, col-s, -1):
      a[row+s][c] = group[index]
      index += 1
    # (r+s, c-s) -> (r-s, c-s)
    for r in range(row+s, row-s, -1):
      a[r][col-s] = group[index]
      index += 1


n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
d = [list(map(int, input().split())) for _ in range(k)]
d = [(r-1, c-1, s) for r, c, s in d]
d.sort()
ans = 100*100

while True:
  b = deepcopy(a)
  for t in d:
    go(b, t)
  for i in range(n):
    s = sum(b[i])
    if ans > s:
      ans = s

  if not next_permutation(d):
    break
print(ans)
