class Progmem:
    def __init__(self):
        self.debug = 0
    def loadBinary(self, filename):
        try:
            self.binary = open(filename, 'rb')
        except FileNotFoundError:
            print(f"File {filename} not found")
    def __getitem__(self, offset):
        # *2 ker beremo 2 byta hkrati, PC 
        offset *= 2
        try:
            self.binary.seek(offset, 0)
            byte1 = int.from_bytes(self.binary.read(1), byteorder='big')
            byte2 = int.from_bytes(self.binary.read(1), byteorder='big')
            if self.debug > 3:
                print(f"offset: {offset}, byte1: {byte1}, byte2: {byte2}, instruction: {hex(byte1*256 + byte2)}")
            return byte1*256 + byte2
        except EOFError:
            return 0