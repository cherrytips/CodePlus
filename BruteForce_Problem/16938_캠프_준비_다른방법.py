# This code has been copied.
n, l, r, x = map(int, input().split())
a = list(map(int, input().split()))


def go(index, cnt, tot, easy, hard):
  if index == n:
    if cnt >= 2 and l <= tot <= r and hard-easy >= x:
      return 1
    else:
      return 0
  cnt1 = go(index+1, cnt+1, tot+a[index], min(easy, a[index]), max(hard, a[index]))
  cnt2 = go(index+1, cnt, tot, easy, hard)
  return cnt1+cnt2


print(go(0, 0, 0, 1000000, 0))
