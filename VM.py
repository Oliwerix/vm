import cmd2
from hw.Proc import Proc
class VM(cmd2.Cmd):
    def __init__(self):
        self.proc = Proc()
        self.__debugLevels = ['0','1','2','3']
        cmd2.Cmd.__init__(self)
    def do_loadBinary(self, line):
        "loadBinary filename \nLoads a binary from file"
        self.proc.loadBinary(line)

    complete_loadBinary = cmd2.Cmd.path_complete
    
    def do_execute(self, line):
        "execute\nExecutes commands from binary until a set breakpoint"
        self.proc.execute()
    def do_setDebug(self, line):
        "setDebug level\nSets the debug level"
        self.proc.debug = int(line)
    def complete_setDebug(self, text, line, begidx, endidx):
        if not text:
            return self.__debugLevels
        
    # def do_EOF(self, line):
    #     return True

    
if __name__ == '__main__':
    VM().cmdloop()