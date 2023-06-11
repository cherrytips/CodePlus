import sys
readline = sys.stdin.readline


def next_permutation(perm):
  i = len(perm)-1
  while i > 0 and perm[i-1] >= perm[i]:
    i -= 1
  if i <= 0:
    return False
  j = len(perm)-1
  while perm[j] <= perm[i-1]:
    j -= 1

  perm[i-1], perm[j] = perm[j], perm[i-1]

  j = len(perm)-1
  while i < j:
    perm[i], perm[j] = perm[j], perm[i]
    i += 1
    j -= 1

  return True


def prev_permutation(perm):
  i = len(perm)-1
  while i > 0 and perm[i-1] <= perm[i]:
    i -= 1
  if i <= 0:
    return False
  j = len(perm)-1
  while perm[j] >= perm[i-1]:
    j -= 1

  perm[i-1], perm[j] = perm[j], perm[i-1]

  j = len(perm)-1
  while i < j:
    perm[i], perm[j] = perm[j], perm[i]
    i += 1
    j -= 1

  return True


def check(perm, a):
  for i in range(len(a)):
    if a[i] == '<' and perm[i] > perm[i+1]:
      return False
    if a[i] == '>' and perm[i] < perm[i+1]:
      return False
  return True


k = int(readline().strip())
a = readline().split()
small = [i for i in range(k+1)]
big = [9-i for i in range(k+1)]

while True:
  if check(small, a):
    break
  if not next_permutation(small):
    break

while True:
  if check(big, a):
    break
  if not prev_permutation(big):
    break

print(''.join(map(str, big)))
print(''.join(map(str, small)))
