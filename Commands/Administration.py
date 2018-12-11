from Command import *


class BanUser (Command):
    def load(self):
        self.name = "ban"
        self.syntax = "<nick:text>"
        self.help = "Set user's permissions"
        self.permissions = Permissions.Admin

    def execute(self, args, caller):
        user = self.get_user_by_nick(self.getStr(args, 0))
        if caller.permissions > user.permissions:
            self.server.ban(user.ip)
            raise CmdAnswer("User {} ({}) banned!".format(
                user.nick,
                user.ip
            ))
