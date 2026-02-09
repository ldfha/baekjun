N, B = map(int, input().split())
formationB = []

formationB.append(N % B)
q = N // B
while q != 0:
    formationB.append(q % B)
    q //= B

if B > 10:
    for b in formationB[::-1]:
        if b >= 10:
            print(chr(b+55), end='')
        else:
            print(b, end='')
else:
    for b in formationB[::-1]:
        print(b, end='')