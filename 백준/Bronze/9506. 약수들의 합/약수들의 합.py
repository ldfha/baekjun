while True:
    n = int(input())
    if n == -1:
        break
    total = 0
    div = []
    for i in range(1, n):
        if n % i == 0:
            total += i
            div.append(i)
            div.append('+')
    if total != n:
        print(f'{n} is NOT perfect.')
        continue
    print(f'{n} =', *div[:-1])