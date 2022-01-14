import cmd
from hw.Proc import Proc
class VM(cmd.Cmd):
    def __init__(self):
        self.proc = Proc()
    