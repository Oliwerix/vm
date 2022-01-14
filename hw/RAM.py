RAM_SIZE = 128

class RAM:
    def __init__(self) -> None:
        self.ram = 0
    def __iter__(self):
        self.__iterator = 0
        return self
    def __next__(self):
        if self.__iterator < RAM_SIZE:
            x = self[self.__iterator]
            self.__iterator += 1
            return x
        else:
            raise StopIteration

    def __getitem__(self, bit_number) -> bool:
        return self.ram & 1 << bit_number != 0
    def __setitem__(self, bit_number, bit) -> None:
        if bit:
            self.ram |= (1 << bit_number)
        else:
            self.ram &= ~(1 << bit_number)

    def getByte(self, byte) -> int:
        return (self.ram & (0xff << (byte * 8))) >> (byte * 8)
    def setByte(self, byte_number, byte) -> None:
        # najprej rabmo clearat byte, pol sele lahko nastaumo
        self.ram &= ~(0xff << byte_number*8)
        self.ram |= (byte << byte_number*8)
    def getPC(self)->int:
        return self.getByte(1)*256 + self.getByte(0)

    def incPC(self) -> int:
        PC = self.getPC()
        PC = (PC + 1) % (256*255)
        self.setByte(1, PC >> 8)
        self.setByte(0, PC % 256)
        # tuki returnamo bl k ne za debug purposes
        return PC
        
    def __str__(self):
        out = ""
        i = 0
        while i < RAM_SIZE / 8:
            out += "{0:#0{1}x}".format(self.getByte(i+1)*256 + self.getByte(i), 6) + '\n'
            i += 2
        return out

    
if __name__ == "__main__":
    ram = RAM() 
    # ram.setByte(3, 0xff)
    print(ram.ram)

    ram[1] = True
    print(ram)
    print(ram.ram)