word = list(input())
isPalin = False
for i in range(len(word)//2 + 1):
    if word[i] == word[-(i+1)]:
        isPalin = True
    else:
        isPalin = False
        break
print(1) if isPalin else print(0) 