n = int(input())

human = input().split()
human = [int(i) for i in human]
human.sort(reverse=True)

group = 0
node = 0

while node < n:
    node += human[node]
    group += 1

print(group)
