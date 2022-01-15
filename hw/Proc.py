from .RAM import RAM
from .Progmem import Progmem

class Proc:
    def __init__(self) -> None:
        self.ram = RAM()
        self.progmem = Progmem()
        self.brakepoints = list()
        # 0 - disabled, 1 - low, 2 - high, 3 - all
        self.__debug = 0
    def loadBinary(self, filename):
        self.progmem.loadBinary(filename)
    def execute(self):
        while  not self.ram.getPC() in self.brakepoints:
            self.executeInstruction()
    def executeInstruction(self):
        instruction = self.progmem[self.ram.getPC()]
        self.ram.incPC()

        op1 = (instruction & 0x7f00) >> 9
        op2 = (instruction & 0x01fc) >> 2
        ins = (instruction & 0x0002) >> 1
        if self.debug > 0:
            print(f"PC: {self.ram.getPC()}")
            print(f"op1: {op1} op2: {op2} instruction: {ins}")
        if ins:
            self.__nand(op1, op2)
        else:
            self.__copyTwoBytes(op1, op2)
        if self.debug > 2:
            print(self.ram)
    def addBrakepoint(self, where):
        self.brakepoints.append(where)
    def __nand(self, source, target):
        bit1 = self.ram[source]
        bit2 = self.ram[target]

        if self.debug > 1:
            print(f" nand: bit1: {bit1}, bit2: {bit2}, nand: {not (bit1 and bit2)}")        
        if self.debug > 2:
            print(f"   source: {source}, target: {target}")
        self.ram[target]= not (bit1 and bit2)

    def __copyTwoBytes(self, source, target):
        bytes = self.ram.getBytes(source, 2)
        if self.debug > 1:
            print(f" copy: source: {source}, target: {target}")
        self.ram.setBytes(target, bytes, 2)
    def __str__(self):
        return f"PC: {self.ram.getPC()}\n RAM: \n {self.ram}"
    @property
    def debug(self):
        return self.__debug
    @debug.setter
    def debug(self, value):
        self.__debug = value
        self.progmem.debug = value
    # @debug.getter
    # def debug(self):
    #     return self.__debug
