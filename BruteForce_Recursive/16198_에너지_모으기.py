import sys
readline = sys.stdin.readline

# o o o o o
# W[i]
# 첫번째 마지막 선택 불가능
# x번째 제거 => return?
# x 번째 양 옆 구슬 에너지를 곱한만큼 에너지 모음
# 구슬 갯수 당연히 감소
# 번호는 1부터 매김 (0부터 아님)

# logic 1: 길이가 2면 더이상 선택 불가능 => 결과 배열에 저장하고 return

N = int(readline().strip())
W = list(map(int, readline().split()))
res = []


def energy(W, cnt):
  if len(W) == 2:  # logic 1
    res.append(cnt)
    return
  for i in range(1, len(W)-1):
    cnt += (W[i-1]*W[i+1])  # 에너지 더하고
    temp = W.pop(i)  # 구슬 삭제

    energy(W, cnt)  # recursive

    W.insert(i, temp)  # 원상복구
    cnt -= (W[i-1]*W[i+1])
  return


energy(W, 0)  # 구슬 배열, 초기 에너지값
print(max(res))
