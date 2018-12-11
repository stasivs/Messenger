from Errors import *
from Permissions import *


class Command:
    # базовый класс, описывающий любую команду

    def __init__(self, server):
        self.name = ""
        self.syntax = ""
        self.help = ""
        self.server = server
        self.permissions = Permissions.Anyone

    def load(self):
        raise NotImplementedError("Load method must be implemented")

    def execute(self, args, caller):
        raise NotImplementedError("Execute method must be implemented")

    def getStr(self, args, index):
        try:
            return args[index]
        except IndexError:
            raise CmdSyntaxError(self)

    def get_user_by_nick(self, nick):
        try:
            u = self.server.get_user_by_nick(nick)
        except ServerError:
            raise CmdError("User with nick {} not found!".format(nick))
        return u
