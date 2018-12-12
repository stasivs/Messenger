from Messages import *
from Command import *


class Setnick (Command):
    def load(self):
        self.name = "setnick"
        self.syntax = "<nick:text>"
        self.help = "Change your nick"
        self.permissions = Permissions.User

    def execute(self, args, caller):
        nick = self.getStr(args, 0)
        try:
            self.get_user_by_nick(nick)
        except CmdError:
            self.server.resend(Bcast("{} ({}) changed nick to {}".format(
                caller.nick,
                caller.ip,
                nick
            )))
            caller.nick = nick
            raise CmdAnswer("Nick successful changed to {}".format(nick))
        else:
            raise CmdError("Nick {} already in use".format(nick))
