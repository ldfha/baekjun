n, x = map(int, input().split())
num_list = list(input().split())
for num in num_list:
    if int(num) < x:
        print(num, end=' ')