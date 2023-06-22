# This code has been copied.
n = 3


def is_magic(d):
  magic = d[0*n+0] + d[0*n+1] + d[0*n+2]
  for i in range(n):
    s = 0
    for j in range(n):
      s += d[i*n+j]
    if magic != s:
      return False
  for j in range(n):
    s = 0
    for i in range(n):
      s += d[i*n+j]
    if magic != s:
      return False
  if magic != d[0*n+0] + d[1*n+1] + d[2*n+2]:
    return False
  if magic != d[0*n+2] + d[1*n+1] + d[2*n+0]:
    return False
  return True


def diff(a, d):
  ans = 0
  for i in range(n*n):
    ans += abs(a[i] - d[i])
  return ans


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


a = []
for i in range(n):
  a += list(map(int, input().split()))
d = list(range(1, n*n+1))
ans = -1

while True:
  if is_magic(d):
    cost = diff(a, d)
    if ans == -1 or ans > cost:
      ans = cost
  if not next_permutation(d):
    break
print(ans)
