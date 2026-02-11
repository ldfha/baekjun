N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
for i in range(N):
    for j in range(i+1, N):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
for n in numbers:
    print(n)