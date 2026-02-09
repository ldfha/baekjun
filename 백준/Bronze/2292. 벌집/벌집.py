# 이웃하는 벌집 갯수 1, 6, 12, 18, ...
# 벌집에 쓰여진 숫자 : 1, 1+(1~6), 7+(1~12), 19+(1~18)
# n0 = 1, n = 3 * n ** 2 - 3 * n + 2, 
N = int(input())
n = 1
while N > 1:
    this = 3 * n ** 2 - 3 * n + 2 
    next = 3 * (n + 1) ** 2 - 3 * (n + 1) + 2 
    n += 1
    if this <= N < next: break
print(n)
