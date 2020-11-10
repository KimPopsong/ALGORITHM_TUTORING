s = input().split()

n = int(s[0])  # Number of List
m = int(s[1])  # Repeat Number
k = int(s[2])  # Limit Repeat

s = input().split()
s = [int(i) for i in s]

s.sort()
first = s[-1]
second = s[-2]

cycle = int(m / (k + 1))
rest = int(m % (k + 1))

sum = cycle * (first * k + second) + rest * first

print(sum)