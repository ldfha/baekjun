N = int(input())
start = 666
count = 0
while True:
    if "666" in str(start):
        count += 1
        if count == N:
            print(start)
            break
    start += 1