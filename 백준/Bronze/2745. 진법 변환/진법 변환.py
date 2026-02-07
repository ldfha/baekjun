N, B = input().split()
decimal = 0
for i in range(len(N)):
    if ord(N[i])>=65:
        n = ord(N[i])-55
    else:
        n = int(N[i])
    decimal += n * (int(B) ** (len(N) - 1 - i))
print(decimal)