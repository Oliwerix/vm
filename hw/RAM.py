RAM_SIZE = 128
STDIO = 0x10
STDIO_SIZE = 4
class RAM:
    def __init__(self) -> None:
        self.__ram = 0
    @property
    def ram(self):
        self.__ram &= ~((2**(STDIO_SIZE)-1) << STDIO_SIZE * STDIO)
        self.__ram |= (self.stdio.stdio << STDIO_SIZE * STDIO)
        return self.__ram
    @ram.setter
    def ram(self, value):
        self.stdio.stdio = self.__ram & ((2**(STDIO)-1) << (STDIO_SIZE * STDIO)) >> (STDIO_SIZE)
        self.__ram = value

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
    def loadStdio(self, what):
        self.stdio = what
    def getBytes(self, byte, how_many=1) -> int:
        "Gets bytes begining with byte"
        return (self.ram & ((2**(8*how_many)-1) << (byte * 8 * how_many))) >> (byte * 8 * how_many)
    def setBytes(self, byte_number, bytes, how_many=1) -> None:
        # najprej rabmo clearat byte, pol sele lahko nastaumo
        self.ram &= ~((2 ** (8 * how_many) - 1) << byte_number * 8 * how_many)
        self.ram |= (bytes << byte_number*8*how_many)
    def getPC(self) -> int:
        "Gets the program counter"
        return self.getBytes(0,2)

    def incPC(self) -> int:
        "Increments the program counter"
        pc = self.getPC()
        pc = (pc + 1) % (256*256)
        self.setBytes(0, pc, 2)
        # tuki returnamo bl k ne za debug purposes
        return pc
        
    def __str__(self):
        out = ""
        i = 0
        while i < RAM_SIZE / 8:
            out += "{0:#0{1}x}".format(self.getBytes(i), 4) +' '
            out += "{0:#0{1}x}".format(self.getBytes(i+1), 4) + '\n'
            i += 2
        return out

    
if __name__ == "__main__":
    from hw.TelnetStdio import TelnetStdio
    ram = RAM() 
    ram.loadStdio(TelnetStdio())
    # ram.setByte(3, 0xff)
    print(ram.ram)

    ram.setBytes(0, 0xffff, 2)
    print(hex(ram.getPC()))
    ram.incPC()
    print()
    print(hex(ram.getPC()))

    # print(ram.ram)