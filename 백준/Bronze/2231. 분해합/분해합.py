N = int(input())
i = 1
while i < N:
# for i in range(N - 1, 0, -1):
    hap = N 
    n_list = str(i)
    for x in n_list:
        hap -= int(x)
    if hap == i:
        print(i)
        break
    i += 1
else:
    print(0)