# This code fails.
import sys
readline = sys.stdin.readline


def check_all_empty(arr):
  for a in arr:
    if a != '':
      return False

  return True


def get_long(arr):
  res = []
  res_index = []
  length = 0
  for i in range(len(arr)):
    if len(arr[i]) > length:
      res.clear()
      res_index.clear()
      length = len(arr[i])
    if len(arr[i]) == length:
      res.append(arr[i])
      res_index.append(i)

  return res, res_index


N = int(readline().strip())
words = []
alph = {}
nums = []
cnt = 9

for _ in range(N):
  words.append(readline().strip())

nums = ['' for _ in range(N)]

while not check_all_empty(words):
  l, li = get_long(words)

  for i in range(len(l)):
    if l[i][0] not in alph.keys():
      alph[l[i][0]] = cnt
      cnt -= 1
    words[li[i]] = words[li[i]][1:]
    nums[li[i]] += str(alph[l[i][0]])

print(sum(list(map(int, nums))))
