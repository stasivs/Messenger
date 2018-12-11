from Errors import *
from Command import *
import os
import sys


class Executor:
    # класс, описывающий обработчик команд

    CmdNotFound = ServerError("Command with name {} not found")

    def __init__(self, server):
        self.server = server
        self.__commands = []

    def reload(self):
        sys.path.append("/Commands")
        lst = os.listdir("/Commands")
        for module in lst:
            try:
                __import__(os.path.splitext(module)[0])
            except Exception as ex:
                print("Executor: not imported", module)
        for c in Command.__subclasses__():
            try:
                cmd = c(self.server)
                cmd.load()
            except Exception as ex:
                print(c.__class__.__name__, "not loaded")
                continue
            self.__commands.append(cmd)

    def execute(self, name, args, caller):
        pass

    def get_command(self, name):
        for cmd in self.__commands:
            if cmd.name == name:
                return cmd
        return Executor.CmdNotFound.formatted(name)
