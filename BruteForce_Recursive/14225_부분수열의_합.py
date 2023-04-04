import sys
readline = sys.stdin.readline

N = int(readline().strip())
S = list(map(int, readline().split()))
possible = set()


def solve(idx, cur):
  possible.add(cur)

  if idx == N:
    return
  solve(idx+1, cur+S[idx])
  solve(idx+1, cur)


solve(0, 0)
for i in range(1, max(possible)+2):
  if i not in possible:
    print(i)
    break
