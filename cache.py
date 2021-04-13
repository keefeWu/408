#coding:utf-8
import math
import random
import numpy

def convertUnit(num):
    if num < 1<<10:
        return str(num)
    if num < 1<<20:
        return str(int(num/(1<<10))) + 'K'
    if num < 1<<30:
        return str(int(num/(1<<20))) + 'M'
    return str(int(num/(1<<30))) + 'G'

class Cache:
    def __init__(self, row = 0, col = 0, rowLead = 0, dataLead = 0, flag = 'direct', groupNum = 0, markLength = 0, memoryAddressCapacity = 0):
        self.row = row
        self.col = col
        self.rowLead = rowLead
        self.dataLead = dataLead
        self.leadNum = 0 
        self.flag = flag
        self.markLength = markLength # 标记位长度
        self.groupNum = groupNum # 组相连映射用到的分组数
        self.memoryAddressCapacity = memoryAddressCapacity
        self.memoryAddressLength = 0
        if memoryAddressCapacity > 0:
            self.memoryAddressLength =  round(math.log(memoryAddressCapacity) / math.log(2))
    
    def getLead(self):
        if self.row <= 0:
            return 0
        if self.col <= 0:
            return 0
        self.rowLead =  round(math.log(self.row) / math.log(2))
        self.dataLead = round(math.log(self.col) / math.log(2))
        self.leadNum = self.rowLead + self.dataLead 
        return self.leadNum
    
    def getCacheAddress(memoryAddr):
        if self.leadNum <= 0:
            self.getLead()
        if self.leadNum <= 0:
            return 0
        if self.flag == 'direct':
            cacheAddr = memoryAddr % self.leadNum # 直接映射就是主存地址直接除以cache总的个数取余数
        if self.flag == 'fully':
            return random.randint(0, leadNum) # 全相连是随机映射的，没有固定搭配，所以这里用随机数做个演示
        if self.flag == 'set':
            if self.groupNum <= 0:
                return 0
            cacheAddr = memoryAddr % self.groupNum # 组号是取余数，组内是随机，未完待续
    
    def setMemoryAddressCapacity(self, memoryAddressCapacity):
        if memoryAddressCapacity > 0:
            self.memoryAddressCapacity = memoryAddressCapacity
            self.memoryAddressLength =  round(math.log(memoryAddressCapacity) / math.log(2))
            if self.leadNum <= 0:
                self.getLead()
            self.markLength = self.memoryAddressLength - self.leadNum

    def allocateCache(self):
        # self.data = np.zeros((self.row,self.col * 8 + 1 + self.markLength)) # 数据字节大小*8为数据位，+1个有效位决定是否工作，+n个标记位
        self.data = np.repeat(np.array('0'* (self.col * 8 + 1 + self.markLength)), self.row) # 数据字节大小*8为数据位，+1个有效位决定是否工作，+n个标记位

    def pushDataToCache(self, memoryAddr, memoryData):
        if self.flag == 'direct':
            # cacheAddr = memoryAddr % self.leadNum # 直接映射就是主存地址直接除以cache总的个数取余数
            # 故意写麻烦一点 
            start = 2 # 0x
            memoryAddr = '0'*(self.memoryAddressLength - len(memoryAddr) + start) + memoryAddr[start:]
            dataAddress = memoryAddr[-self.dataLead:]
            row = memoryAddr[-self.rowLead - self.dataLead :-self.dataLead]
            mark = memoryAddr[start: start + self.markLength]
            data = memoryData[int('0b' + memoryAddr,2)][int('0b' + dataAddress,2) * 8: (int('0b' + dataAddress,2) + 1) * 8]
            temp = str(self.data[int('0b' + row, 2)])
            temp = '1' + temp[1:]
            temp = temp[:1] + mark + temp[self.markLength:]
            temp = temp[:self.markLength + int('0b' + dataAddress,2) * 8] + data + temp[self.markLength + (int('0b' + dataAddress,2) + 1) * 8 :]
            
            self.data[int('0b' + row, 2)] = temp
            
    
cache = Cache(row = 8, col = 64)
cache.setMemoryAddressCapacity(256<<20)
print(cache.markLength)
cache.allocateCache()

memoryData = np.repeat(np.array('1'* (64 << 3)), 256 << 8)
# memoryData = np.random.randint(0,2, size=(256, 64 << 3)) # 内存大小256MB
cache.pushDataToCache(bin(int('0x0000056',16)), memoryData)


