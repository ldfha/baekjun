n, m = map(int, input().split())
basket = []
for i in range(n):
    basket.append(0)

for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i-1, j): # i번 바구니부터 j번 바구니까지
        if basket[l] == 0 or basket[l] != k:
            basket[l] = k

print(*basket)