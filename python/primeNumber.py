# 判断是否质数
def is_prime(x):
    if x == 2:
        return True
    elif x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

def getPrimeArray(x, maxNum):
    primeArray = []
    for i in range(1, maxNum+1):
        if i == x:
            continue
        if is_prime(x+i):
            primeArray.append(i)
    return primeArray

class Data:
    def __init__(self, maxNum):
        self.neighborArray = []
        self.maxNum = maxNum
        self.pre = 0
        self.idx = -1
    def next(self):
        return self.neighborArray[self.idx]

def getPossibleValue(data, statusArray): # 在当前层找到这一层可以出的一个值
    isFind = False
    value = 0
    for i in range(data.idx+1, len(data.neighborArray)):
        if statusArray[data.neighborArray[i]-1] == 0: # 找到了
            data.idx = i
            isFind = True
            value = data.neighborArray[i]
            statusArray[value - 1] = 1
            break
        else:
            continue
    return isFind, value

def back(dataList, i, statusArray):
    statusArray[i] = 0
    dataList[i].idx = -1
    i = dataList[i].pre

    if dataList[i].idx < len(dataList[i].neighborArray) - 1:
        isFind, value = getPossibleValue(dataList[i], statusArray)
        if isFind:
            next = value - 1
            statusArray[value - 1] = 1
            dataList[next].pre = i
            i = next
            return i
    if i == dataList[i].pre:
        return i
    # i = dataList[i].pre
    i = back(dataList, i, statusArray)
    return i
        
def getResult(dataList, maxNum):
    result = [1] * maxNum
    # print(result[0])
    i = 1
    for idx in range(maxNum-1):
        i = dataList[i-1].neighborArray[dataList[i-1].idx]
        result[idx+1] = i
        # print(result[idx])
    return is_prime(result[-1] + result[0]), result

maxNum = 20
# 算出每个数字的潜在邻居
dataList = []
for i in range(1,maxNum+1):
    neighborArray = getPrimeArray(i, maxNum)
    data = Data(maxNum)
    data.neighborArray = neighborArray
    dataList.append(data)
    # print(i, data.neighborArray)

# 深度优先顺着邻居遍历，遇到环了就后退
statusArray = [0] * maxNum # 排好一个数就把那一位置为1，否则为0
resultList = [] # 存放结果
i = 0 # 层数
start = True
statusArray[0] = 1
while dataList[0].idx < len(dataList[i].neighborArray) - 1 or statusArray[0] != 1 or sum(statusArray)!=1:
    start = False
    isFind, value = getPossibleValue(dataList[i], statusArray)
    if isFind:
        next = value - 1
        dataList[next].pre = i
        i = next
    else:
        if maxNum == sum(statusArray): # 找齐了
            status, result = getResult(dataList, maxNum)
            if status:
                resultList.append(result)
                print(result)
            # if dataList[0].idx == len(dataList[i].neighborArray) - 1 and  sum(statusArray) == maxNum:
            #     break
        i = back(dataList, i, statusArray)

# for i in range(maxNum):
#     print(dataList[i].neighborArray[dataList[i].idx])
# for result in resultList:
#     print(result)
            
print(len(resultList))



#     for j in range(len(dataList[i].neighborArray)):
#         if 0 == statusArray[dataList[i].neighborArray[j]]:
#             isFind = True
#             break
#         else:
#             continue
#     # 如果当前层没有找到，说明有环了
#     if not isFind:
#         if i == maxNum:
#             pass # 找到了，这里顺势把结果输出出来
#         else:
#             # 如果没找到且还没有到底，说明前面一步该+1了
#             i -= 1

#     dataList[i].next = j
# for i in range(maxNum):
#     while statusArray[dataList[i].neighborArray[]]
#     while j
#     for j in range(len(dataList[i].neighborArray)):
#         idx = 
#         print(j)



