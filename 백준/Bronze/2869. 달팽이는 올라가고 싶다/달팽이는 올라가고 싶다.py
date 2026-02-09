A, B, V = map(int, input().split())
up = A - B 
d = (V - A) / (A - B)
day = round(d) + 1 if round(d) < d else round(d)
while True:
    v = V - up * day
    if v <= A:
        print(day+1)
        break
    else:
        day += 1