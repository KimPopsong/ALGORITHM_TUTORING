n = int(input())
grade = []

for i in range(0, n):
    name = input()

    for j in range(0, len(name)):
        if(name[j] == ' '):
            score = int(name[j + 1:])
            name = name[0:j]
            break

    temp = []
    temp.append(name)
    temp.append(score)

    grade.append(temp)

for i in range(0, n - 1):
    for j in range(0, n - 1):
        if grade[j][1] > grade[j + 1][1]:
            grade[j], grade[j + 1] = grade[j + 1], grade[j]

for i in range(0, n):
    print(grade[i][0], end=' ')