# This code has been copied.
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


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
people = []
store = []
for i in range(n):
  for j in range(n):
    if a[i][j] == 1:
      people.append((i, j))
    elif a[i][j] == 2:
      store.append((i, j))
d = [0]*len(store)
for i in range(m):
  d[i] = 1
d.sort()
ans = -1
while True:
  s = 0
  for px, py in people:
    dists = []
    for i, (sx, sy) in enumerate(store):
      if d[i] == 0:
        continue
      d1 = abs(px-sx)
      d2 = abs(py-sy)
      dists.append(d1+d2)
    dists.sort()
    s += dists[0]
  if ans == -1 or ans > s:
    ans = s
  if not next_permutation(d):
    break
print(ans)
