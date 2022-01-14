import socket
class Stdio:
    def __init__(self) -> None:
        self.readAvailable = False
        self.writeAvailable = False
        self.__connections = []
        self.__inbuffer = ""
        self.__outbuffer = ""
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


if __name__ == "__main__":
    s = Stdio()
    s.startTelnetServer()