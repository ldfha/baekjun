x = int(input())    # 금액
n = int(input())    # 갯수
datas = []          # 가격 개수
for i in range(n):
    datas.append(input())
total_price = 0
for data in datas:
    price, count = map(int, data.split())
    total_price += price*count
if total_price == x:
    print("Yes")
else:
    print("No")