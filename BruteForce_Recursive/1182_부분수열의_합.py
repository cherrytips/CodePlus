import sys
readline = sys.stdin.readline

N, S = map(int, readline().split())
nums = list(map(int, readline().split()))
res = 0


def solve(index, cur):
  global res

  if index == N:
    if cur == S:
      res += 1
    return

  solve(index+1, cur+nums[index])
  solve(index+1, cur)


solve(0, 0)
if S == 0:
  res -= 1
print(res)
