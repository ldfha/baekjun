import sys
n = int(input())
str = []
for i in range(n):
    str.append(sys.stdin.readline().rstrip())
# print('str',str)
for s in str:
    a, b = map(int, s.split())
    print(a+ b)