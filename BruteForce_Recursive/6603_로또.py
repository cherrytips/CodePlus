import sys
readline = sys.stdin.readline

COUNT = 6


def solve(a, index, lotto):  # 모든 수들, 인덱스, 가능 로또
  if len(lotto) == COUNT:
    print(' '.join(map(str, lotto)))
    return
  if index == len(a):
    return
  solve(a, index+1, lotto+[a[index]])
  solve(a, index+1, lotto)


while True:
  n, *a = list(map(int, readline().split()))
  if n == 0:
    break
  solve(a, 0, [])
  print()
