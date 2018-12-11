from Command import *


class Help (Command):
    def load(self):
        self.name = "help"
        self.syntax = "[name]"
        self.help = "Returns commands list or help for one command"
        self.permissions = Permissions.Anyone

    def execute(self, args, caller):
        if len(args) == 0:
            names = [cmd.name for cmd in self.server.executor.get_list_commands()]
            raise CmdAnswer(", ".join(names))
        else:
            name = self.getStr(args, 0)
            cmd = self.server.executor.get_command(name)
            raise CmdAnswer("Help: /{} {} - {}".format(
                cmd.name,
                cmd.syntax,
                cmd.help
            ))
