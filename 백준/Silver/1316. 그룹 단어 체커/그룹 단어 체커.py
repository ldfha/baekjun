N = int(input())
count = 0
for _ in range(N):
    word = input()
    prev_char = word[0]
    block_char = [word[0]]
    isBlock = False
    isBlockWord = True
    for i in range(1, len(word)):
        if not isBlockWord:
            break

        isBlock = True if word[i] == prev_char else False
        # if word[i] == prev_char:
        #     isBlock = True
        # else :
        #     isBlock = False

        if not isBlock:
            isDu = False
            for c in block_char:
                if c == word[i]:
                    isBlockWord = False
                    isDu = True
                    break
            if not isDu:
                block_char.append(word[i])
        prev_char = word[i]
    if isBlockWord:
        count += 1

print(count)