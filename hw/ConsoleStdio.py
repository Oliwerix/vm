import socket

class ConsoleStdio:
    def __init__(self) -> None:
        self.iinAvailable = False
        self.__outAvailable = False # not used
        self.__outBit = False
        self.__inBuffer = []

    @property
    def inBuffer(self):
        if not len(self.__inBuffer) > 0:
            indata = input("Input: ")
            for char in indata:
                if char in ['0', '1']:
                    self.__inBuffer.append(False if char == '0' else True)
        return self.__inBuffer

    @property
    def inAvailable(self):
        if self.iinAvailable == False:
            self.inBit = self.inBuffer.pop()
            self.iinAvailable = True
            return True
        return True
    @inAvailable.setter
    def inAvailable(self, value):
        if not value:
            self.iinAvailable == False
    @property
    def outBit(self):
        return self.__outBit
    @outBit.setter
    def outBit(self, value):
        self.__outBit = value
        
    @property
    def outAvailable(self):
        return False

    @outAvailable.setter
    def outAvailable(self, value):
        if value:
            print('1' if self.__outBit else '0')


    @property
    def stdio(self) -> int:
        o = 0
        o += self.inAvailable << 3
        o += self.inBit << 2
        o += self.outAvailable << 1
        o += self.outBit
        return o
    @stdio.setter
    def stdio(self, value) -> None:
        o = 0
        self.inAvailable = extractBit(value, 3)
        # self.inBit = extractBit(value, 2)
        self.outAvailable = extractBit(value, 1)
        self.outBit = extractBit(value, 0)
if __name__ == "__main__":
    s = ConsoleStdio()

def extractBit(number, bit):
    return (number & (1<< bit)) >> bit
