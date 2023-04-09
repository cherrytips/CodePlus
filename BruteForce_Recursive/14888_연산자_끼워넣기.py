import sys
readline = sys.stdin.readline


def calc(a, index, cur, plus, minus, mul, div):
  if index == len(a):
    return (cur, cur)
  res = []
  if plus > 0:
    res.append(calc(a, index+1, cur+a[index], plus-1, minus, mul, div))
  if minus > 0:
    res.append(calc(a, index+1, cur-a[index], plus, minus-1, mul, div))
  if mul > 0:
    res.append(calc(a, index+1, cur*a[index], plus, minus, mul-1, div))
  if div > 0:
    if cur >= 0:
      res.append(calc(a, index+1, cur//a[index], plus, minus, mul, div-1))
    else:
      res.append(calc(a, index+1, -(-cur//a[index]), plus, minus, mul, div-1))
  ans = (
      max([t[0] for t in res]),
      min([t[1] for t in res])
  )

  return ans


n = int(readline().strip())
a = list(map(int, readline().split()))
plus, minus, mul, div = map(int, readline().split())
ans = calc(a, 1, a[0], plus, minus, mul, div)

print(ans[0])
print(ans[1])
