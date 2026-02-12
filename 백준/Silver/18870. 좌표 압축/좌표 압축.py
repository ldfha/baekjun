import sys
input = sys.stdin.readline

N = int(input())

points = list(map(int, input().split()))
sorted_point = sorted(set(points))

compress = {value : index for index, value in enumerate(sorted_point)}
for p in points:
    print(compress[p], end=' ')