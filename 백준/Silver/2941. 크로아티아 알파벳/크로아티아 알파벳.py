c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
count = 0
i = 0

while i < len(word):
    isSame = False
    for c in c_alpha:
        if i <= len(word)-len(c) and c[0] == word[i]:     # 목록 글자 중 첫 글자랑 일치하는 경우
            for j in range(1, len(c)):
                if c[j] == word[i+j]:
                    isSame = True
                else:
                    isSame = False
                    break
        if isSame:
            count += 1
            i += len(c) - 1
            break
    if not isSame:
        count += 1

    i += 1

print(count)