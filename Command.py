from Errors import *


class Command:
    # базовый класс, описывающий любую команду

    wrongUsage = CmdError("Wrong usage!")

    def __init__(self, server):
        self.name = ""
        self.syntax = ""
        self.help = ""
        self.server = server

    def load(self):
        raise NotImplementedError("Load method must be implemented")

    def execute(self, args):
        raise NotImplementedError("Execute method must be implemented")

    def getStr(self, args, index):
        try:
            return args[index]
        except IndexError:
            raise Command.wrongUsage
