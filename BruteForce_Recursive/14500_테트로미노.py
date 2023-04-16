# This code fails.
import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
paper = list(list(map(int, readline().split())) for _ in range(N))
max_res = 0


def get_sum(yi, xi):
  temp = 0
  for i in range(4):
    if yi[i] >= N or xi[i] >= M:
      return 0
    temp += paper[yi[i]][xi[i]]

  return temp


def a(y, x):  # 일자
  res = []
  yi = [y, y, y, y]
  xi = [x, x+1, x+2, x+3]
  res.append(get_sum(yi, xi))  # 원본

  yi = [y, y+1, y+2, y+3]
  xi = [x, x, x, x]
  res.append(get_sum(yi, xi))  # 90도 회전

  return max(res)


def b(y, x):  # 사각형
  yi = [y, y, y+1, y+1]
  xi = [x, x+1, x, x+1]
  res = get_sum(yi, xi)  # 원본만 필요

  return res


def c(y, x):  # L 자
  res = []
  yi = [y, y+1, y+2, y+2]
  xi = [x, x, x, x+1]
  res.append(get_sum(yi, xi))  # 원본

  yi = [y, y+1, y+2, y+2]
  xi = [x, x, x, x-1]
  res.append(get_sum(yi, xi))  # 좌우 대칭

  yi = [y, y+1, y+2, y]
  xi = [x, x, x, x+1]
  res.append(get_sum(yi, xi))  # 상하 대칭

  yi = [y, y, y+1, y+2]
  xi = [x, x+1, x+1, x+1]
  res.append(get_sum(yi, xi))  # 상하 좌우 대칭

  yi = [y, y, y, y-1]
  xi = [x, x+1, x+2, x+2]
  res.append(get_sum(yi, xi))  # 좌측 90도 회전

  yi = [y, y, y, y+1]
  xi = [x, x+1, x+2, x]
  res.append(get_sum(yi, xi))  # 우측 90도 회전

  yi = [y, y+1, y+1, y+1]
  xi = [x, x, x+1, x+2]
  res.append(get_sum(yi, xi))  # 좌측 90도 회전 대칭

  yi = [y, y, y, y+1]
  xi = [x, x+1, x+2, x+2]
  res.append(get_sum(yi, xi))  # 우측 90도 회전 대칭

  return max(res)


def d(y, x):
  res = []
  yi = [y, y+1, y+1, y+2]
  xi = [x, x, x+1, x+1]
  res.append(get_sum(yi, xi))  # 원본 == 상하 좌우 대칭

  yi = [y, y+1, y+1, y+2]
  xi = [x, x, x-1, x-1]
  res.append(get_sum(yi, xi))  # 좌우 대칭 == 상하 대칭

  yi = [y, y, y-1, y-1]
  xi = [x, x+1, x+1, x+2]
  res.append(get_sum(yi, xi))  # 좌측 90도 회전 == 우측 90도 회전

  yi = [y, y, y+1, y+1]
  xi = [x, x+1, x+1, x+2]  # 대칭 후 좌측 90도 회전 == 대칭 후 우측 90도 회전

  return max(res)


def e(y, x):
  res = []
  yi = [y, y, y, y+1]
  xi = [x, x+1, x+2, x+1]
  res.append(get_sum(yi, xi))  # 원본 == 볼록 아래

  yi = [y, y, y, y-1]
  xi = [x, x+1, x+2, x+1]
  res.append(get_sum(yi, xi))  # 볼록 위

  yi = [y, y-1, y, y+1]
  xi = [x, x+1, x+1, x+1]
  res.append(get_sum(yi, xi))  # 볼록 좌측

  yi = [y, y-1, y, y+1]
  xi = [x+1, x, x, x]
  res.append(get_sum(yi, xi))  # 볼록 우측

  return max(res)


for i in range(N):
  for j in range(M):
    max_res = max(max_res, max([a(i, j), b(i, j), c(i, j), d(i, j), e(i, j)]))

print(max_res)
