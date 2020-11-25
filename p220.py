storageNum = int(input())  # Number of storage
storages = list(map(int, input().split()))  # Food in storages

dynamicList = [0 for i in range(storageNum)]

dynamicList[0] = storages[0]
dynamicList[1] = max(storages[0], storages[1])

for i in range(2, storageNum):
    dynamicList[i] = max(dynamicList[i - 2] + storages[i], dynamicList[i - 1])

print(dynamicList[-1])
