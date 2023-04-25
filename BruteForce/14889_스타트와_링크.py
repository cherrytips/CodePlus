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


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [0 if i < n/2 else 1 for i in range(n)]
ans = 2147483647
while True:
  first = []
  second = []
  for i in range(n):
    if b[i] == 0:
      first.append(i)
    else:
      second.append(i)
  one = 0
  two = 0
  for i in range(n//2):
    for j in range(n//2):
      if i == j:
        continue
      one += a[first[i]][first[j]]
      two += a[second[i]][second[j]]
  diff = abs(one-two)
  if ans > diff:
    ans = diff
  if not next_permutation(b):
    break
print(ans)
