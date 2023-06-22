# This code has been copied.
n = 3


def diff(a, d):
  ans = 0
  for i in range(n*n):
    ans += abs(a[i] - d[i])
  return ans


magic = [
    [8, 1, 6, 3, 5, 7, 4, 9, 2],
    [6, 1, 8, 7, 5, 3, 2, 9, 4],
    [4, 3, 8, 9, 5, 1, 2, 7, 6],
    [2, 7, 6, 9, 5, 1, 4, 3, 8],
    [2, 9, 4, 7, 5, 3, 6, 1, 8],
    [4, 9, 2, 3, 5, 7, 8, 1, 6],
    [6, 7, 2, 1, 5, 9, 8, 3, 4],
    [8, 3, 4, 1, 5, 9, 6, 7, 2]
]

a = []
for i in range(n):
  a += list(map(int, input().split()))
d = list(range(1, n*n+1))
ans = -1

for d in magic:
  cost = diff(a, d)
  if ans == -1 or ans > cost:
    ans = cost

print(ans)
