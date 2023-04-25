# This code fails.
# import sys
# readline = sys.stdin.readline


# def check_all_empty(arr):
#   for a in arr:
#     if a != '':
#       return False

#   return True


# def get_long(arr):
#   res = []
#   res_index = []
#   length = 0
#   for i in range(len(arr)):
#     if len(arr[i]) > length:
#       res.clear()
#       res_index.clear()
#       length = len(arr[i])
#     if len(arr[i]) == length:
#       res.append(arr[i])
#       res_index.append(i)

#   return res, res_index


# N = int(readline().strip())
# words = []
# alph = {}
# nums = []
# cnt = 9

# for _ in range(N):
#   words.append(readline().strip())

# nums = ['' for _ in range(N)]

# while not check_all_empty(words):
#   l, li = get_long(words)

#   for i in range(len(l)):
#     if l[i][0] not in alph.keys():
#       alph[l[i][0]] = cnt
#       cnt -= 1
#     words[li[i]] = words[li[i]][1:]
#     nums[li[i]] += str(alph[l[i][0]])

# print(sum(list(map(int, nums))))

# This code occurs Time Limit Exceed.
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


def calc(a, letters, d):
  m = len(letters)
  ans = 0
  alpha = dict()
  for i in range(m):
    alpha[letters[i]] = d[i]
  for s in a:
    now = 0
    for x in s:
      now = now * 10 + alpha[x]
    ans += now
  return ans


n = int(input())
a = ['']*n
letters = set()
for i in range(n):
  a[i] = input()
  letters |= set(a[i])
letters = list(letters)
m = len(letters)
d = [i for i in range(9, 9-m, -1)]
d.sort()
ans = 0
while True:
  now = calc(a, letters, d)
  if ans < now:
    ans = now
  if not next_permutation(d):
    break
print(ans)
