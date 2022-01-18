import socket

class TelnetStdio:
    def __init__(self) -> None:
        self.inAvailable = False
        self.inBit = False
        self.outAvailable = False
        self.outBit = False
        self.__connections = []
        self.__inbuffer = ""
        self.__outbuffer = ""
        self.startTelnetServer()
        
    def startTelnetServer(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setblocking(False)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(('127.0.0.1', 5000))
        self.server.listen(5)
    def doTelnetStep(self):
        try:
            connection, address = self.server.accept()
            connection.setblocking(False)
            self.__connections.append(connection)
        except BlockingIOError:
            pass

        for connection in self.__connections:
            try:
                self.__inbuffer += str(connection.recv(4096))
            except BlockingIOError:
                continue
            
            # for connection in self.__connections:
            #     connection.send()
    @property
    def stdio(self) -> int:
        self.doTelnetStep()
        o = 0
        o += self.inAvailable << 3
        o += self.inBit << 2
        o += self.outAvailable << 1
        o += self.outBit
        return o
    @stdio.setter
    def stdio(self, value) -> None:
        o = 0
        # self.inAvailable = extractBit(value, 3)
        # self.inBit = extractBit(value, 2)
        self.outAvailable = extractBit(value, 1)
        self.outBit = extractBit(value, 0)
if __name__ == "__main__":
    s = TelnetStdio()
    s.startTelnetServer()

def extractBit(number, bit):
    return (number & (1<< bit)) >> bit
