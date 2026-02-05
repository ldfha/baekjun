corns = list(map(int, input().split()))
N, KWF = map(int, input().split())
hap = 0
for i in range(0, 10, 2):
    hap += corns[i] * corns[i + 1]

avg = hap // 5
print(avg * N // KWF)