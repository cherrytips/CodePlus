# This code has been copied.
a, b = map(int, input().split())
i = 1
while a <= b:
  if a == b:
    print(i)
    exit()
  if b % 10 == 1:
    b = (b-1)//10
  elif b % 2 == 0:
    b = b//2
  else:
    break
  i += 1
print(-1)
