n = int(input()) #숫자 입력
number = [] #배열

for i in range(0, n):
    k = int(input()) #숫자로 변환 후 배열에 넣어주기
    number.append(k)

for i in range(0, n - 1): #버블 정렬
    for j in range(0, n - 1):
        if number[j] < number[j + 1]: #큰 수 순으로
            number[j], number[j + 1] = number[j + 1], number[j]

for i in range(0, n):
    print(number[i], end=' ')
