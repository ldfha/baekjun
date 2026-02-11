import sys
input = sys.stdin.readline
# 힙정렬 : 오름차순 -> 최소힙(꼭대기가 최소)
# 최대힙생성
def heapify(numbers, idx, size): 
    while True:
        left = 2 * idx + 1
        right = 2 * idx + 2
        largest = idx
        # 왼쪽 자식이 범위 안이고 더 크면
        if left < size and numbers[left] > numbers[largest]:
            largest = left

        # 오른쪽 자식이 범위 안이고 더 크면
        if right < size and numbers[right] > numbers[largest]:
            largest = right

        # 더 이상 바꿀 필요 없으면 종료
        if largest == idx:
            break

        # swap
        numbers[idx], numbers[largest] = numbers[largest], numbers[idx]
        idx = largest

N = int(input())

numbers = []

numbers = [int(input()) for _ in range(N)]

for i in range(N // 2 - 1, -1, -1):
    heapify(numbers, i, N)

for i in range(N - 1, 0, -1):
    numbers[i], numbers[0] = numbers[0], numbers[i]
    heapify(numbers, 0, i)
    
for n in numbers:
    print(n)