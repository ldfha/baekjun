grade_to_score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

chihun = []
for _ in range(20):
    chihun.append(list(input().split()))

total = 0
hakjum = 0
for x in chihun:
    if x[2] != 'P':
        hakjum += float(x[1])
        total += float(x[1]) * grade_to_score[x[2]]

avg_grade = total / hakjum

print(avg_grade)