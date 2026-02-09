N = int(input())
numbers = list(map(int, input().split()))
count = 0
for n in numbers:
    if n == 1:
        continue
    i = 2
    while i < n:
        if n % i == 0:
            break
        i += 1
    else:
        count += 1
    for i in range(2, n):
        if n % i == 0:
            break

print(count)