CHANGE = [25, 10, 5, 1]
T = int(input())
for _ in range(T):
    change=[0,0,0,0]
    C = int(input())
    for i in range(len(CHANGE)):
        if C >= CHANGE[i]:
            change[i] = C // CHANGE[i]
            C %= CHANGE[i]
    print(*change)