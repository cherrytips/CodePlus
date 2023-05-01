# This code has been copied.
def count(words):
  cnt = 0
  for word in words:
    ok = True
    for x in word:
      if not learn[ord(x)-ord('a')]:
        ok = False
        break
    if ok:
      cnt += 1
  return cnt


def go(index, k, words):
  if k < 0:
    return 0
  if index == 26:
    return count(words)
  ans = 0
  learn[index] = True
  t1 = go(index+1, k-1, words)
  learn[index] = False
  if ans < t1:
    ans = t1
  if index not in [ord('a')-ord('a'), ord('n')-ord('a'), ord('t')-ord('a'), ord('i')-ord('a'), ord('c')-ord('a')]:
    t2 = go(index+1, k, words)
    if ans < t2:
      ans = t2
  return ans


n, m = map(int, input().split())
words = [input() for _ in range(n)]
learn = [False] * 26
print(go(0, m, words))
