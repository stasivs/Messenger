from Command import *


class PermSet (Command):
    def load(self):
        self.name = "permset"
        self.syntax = "<nick:text> <group:text>"
        self.help = "Set user's permissions"
        self.permissions = Permissions.Admin

    def execute(self, args, caller):
        user = self.get_user_by_nick(self.getStr(args, 0))
        perm = self.getStr(args, 1).lower().capitalize()
        if perm not in Permissions.Perms:
            raise CmdError("Group {} not found!".format(perm))
        if Permissions.Perms.index(perm) < caller.permissions and caller.permissions > user.permissions:
            user.permissions = Permissions.Perms.index(perm)
            raise CmdAnswer("Successful set {} permissions to {}".format(
                user.nick,
                perm
            ))
        raise CmdError("You can only set permissions lower than yours!")


class PermInfo (Command):
    def load(self):
        self.name = "perminfo"
        self.syntax = "<nick:text>"
        self.help = "Returns user's permissions"
        self.permissions = Permissions.User

    def execute(self, args, caller):
        user = self.get_user_by_nick(self.getStr(args, 0))
        raise CmdAnswer("{} permissions is {}".format(
            user.nick,
            Permissions.Perms[user.permissions]
        ))
