str = input().upper()
ss = set(str)
cnt = {}
for s in ss:
    cnt[s] = str.count(s)
m = max(cnt.values())
M = [k for k, v in cnt.items() if v == m]
if len(M) == 1:
    print(*M)
else :
    print('?')