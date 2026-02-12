import sys
input = sys.stdin.readline
# counting 정렬
N = int(input())
counting = [0] * 10001  # 카운팅 배열, 최대값은 10,000
for _ in range(N):
    num = int(input())
    counting[num] += 1      # 원소 개수 업데이트

for i in range(10001):
    if counting[i] != 0:
        for _ in range(counting[i]):
            print(i)