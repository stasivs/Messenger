from Command import *
from Messages import *


class BanUser (Command):
    def load(self):
        self.name = "ban"
        self.syntax = "<nick:text>"
        self.help = "Ban user's IP and kick user from server"
        self.permissions = Permissions.Admin

    def execute(self, args, caller):
        user = self.get_user_by_nick(self.getStr(args, 0))
        if caller.permissions > user.permissions:
            self.server.ban(user.ip)
            user.disconnect()
            self.server.resend(Bcast("{} banned {} ({})".format(
                caller.nick,
                user.nick,
                user.ip
            )))
            raise CmdAnswer("User {} ({}) banned!".format(
                user.nick,
                user.ip
            ))


class UnbanIP (Command):
    def load(self):
        self.name = "unban"
        self.syntax = "<ip:text>"
        self.help = "Unban IP"
        self.permissions = Permissions.Admin

    def execute(self, args, caller):
        ip = self.getStr(args, 0)
        self.server.unban(ip)
        self.server.resend(Bcast("{} unbanned IP {}".format(
            caller.nick,
            ip
        )))
        raise CmdAnswer("Successful unbanned IP {}".format(ip))


class Kick (Command):
    def load(self):
        self.name = "kick"
        self.syntax = "<nick:text>"
        self.help = "Kick user from server"

    def execute(self, args, caller):
        user = self.get_user_by_nick(self.getStr(args, 0))
        user.disconnect()
        self.server.resend(Bcast("{} kicked {} ({})".format(
            caller.nick,
            user.nick,
            user.ip
        )))
