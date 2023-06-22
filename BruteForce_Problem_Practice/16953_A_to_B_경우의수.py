# This code has been copied.
def go(a, b):
  if a == b:
    return 1
  if a > b:
    return -1
  t1 = go(a*2, b)
  t2 = go(a*10+1, b)
  if t1 == -1 and t2 == -1:
    return -1
  if t1 == -1:
    return t2+1
  if t2 == -1:
    return t1+1
  return min(t1, t2)+1


a, b = map(int, input().split())
print(go(a, b))
