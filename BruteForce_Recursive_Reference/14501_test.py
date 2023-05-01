import sys
readline = sys.stdin.readline

# 모든 일자를 돌면서 최대 수익 구하기
# 다음 상담 가능 일자 : 현재 index + T[index]
# 재귀로 금액(P) 을 구해서 결과 배열에 우선 저장
# !!주의!!
# "바로 다음 순서의 상담을 반드시 진행할 필요는 없다."

N = int(readline().strip())
T, P = [], []
for _ in range(N):
  t, p = map(int, readline().split())
  T.append(t)
  P.append(p)
ans = []  # 결과값 저장 배열
# print(N, T, P)


def council(idx, cnt):
  if idx < N:
    if N < idx+T[idx]:  # 당일 상담 시 마지막 날을 넘어갈 경우 회사에 없다
      ans.append(cnt)
      return
    elif N == idx+T[idx]:  # 마지막 날까지 상담 가능한 경우 마지막날 수익을 더한다
      ans.append(cnt+P[idx])
      return
  elif N <= idx:
    ans.append(cnt)
    return
  for i in range(N):
    council(idx+T[idx]+i, cnt + P[idx])
  return


for i in range(N):
  council(i, 0)

# print(ans)
print(max(ans))
