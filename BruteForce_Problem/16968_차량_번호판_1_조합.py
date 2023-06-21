# This code has been copied.
s = input()
ans = 1
for i in range(len(s)):
  cnt = 26 if s[i] == 'c' else 10
  if i > 0 and s[i] == s[i-1]:
    cnt -= 1

  ans = ans * cnt
print(ans)
