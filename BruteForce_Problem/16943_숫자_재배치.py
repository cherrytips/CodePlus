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


a, b = input().split()
a = list(a)
b = int(b)
ans = -1
a.sort()

while True:
  c = int(''.join(a))
  if a[0] != '0' and c < b:
    if ans == -1 or ans < c:
      ans = c
  if not next_permutation(a):
    break
print(ans)
