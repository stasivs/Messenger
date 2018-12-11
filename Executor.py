from Command import *
from Errors import *
import os
import sys


class Executor:
    # класс, описывающий обработчик команд

    def __init__(self, server):
        self.server = server
        self.__commands = []
        self.reload()

    def reload(self):
        sys.path.append("Commands")
        lst = os.listdir("Commands")
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
        try:
            try:
                cmd = self.get_command(name)
                if caller.permissions < cmd.permissions:
                    raise CmdNotPermissions("Not enough permissions!")
                cmd.execute(args, caller)
            except CmdCallback as cb:
                caller.send(cb.get_message())
        except ServerError as se:
            print("Error:", se.get_text())

    def get_command(self, name):
        for cmd in self.__commands:
            if cmd.name == name:
                return cmd
        raise CmdNotFound("Command {} not found!".format(name))

    def get_list_commands(self):
        return self.__commands.copy()
