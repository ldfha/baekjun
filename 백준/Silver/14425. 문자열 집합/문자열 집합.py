string_set = set()
count = 0
N, M = map(int, input().split())
for _ in range(N):
    string_set.add(input())
for _ in range(M):
    word = input()
    if word in string_set:
        count += 1
print(count)