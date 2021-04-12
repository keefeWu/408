#coding:utf-8
def convertUnit(num):
    import math
    if num < 1<<10:
        return str(num)
    if num < 1<<20:
        return str(int(num/(1<<10))) + 'K'
    if num < 1<<30:
        return str(int(num/(1<<20))) + 'M'
    return str(int(num/(1<<30))) + 'G'

class MemoryChip:
    def __init__(self, width = 0, length = 0):
        self.width = width
        self.length = length

class Memory:
    def __init__(self, chip = None, row = 0, col = 0):
        self.row = row
        self.col = col
        self.chip = chip
        self.width = 0
        self.length = 0
        self.wordWidth = 0
        self.capacity = 0

    def getCapacity(self):
        self.width = self.getWidth()
        self.length = self.getLength()
        return self.width, self.length
    
    def getWidth(self):
        if self.width <= 0:
            self.width = self.col * self.chip.width
        return self.width
    
    def getLength(self):
        if self.length > 0:
            return self.length
        if self.chip != None:
            self.length = self.row * self.chip.length
        if self.width > 0 and self.capacity > 0:
            self.length = self.capacity / self.width
        return self.length
    
    def getUnitByWord(self):
        return self.getLength()
    
    def getUnitByHalfWord(self):
        return self.getLength() * 2
    
    def getUnitByByte(self):
        return self.getLength() * self.getWidth()

    def setCapacity(self, capacity):
        self.capacity = capacity
    
    def setWidth(self, width):
        self.width = width
    

memory = Memory()
memory.setCapacity(128<<23)
memory.setWidth(64)
convertUnit(memory.getUnitByWord())