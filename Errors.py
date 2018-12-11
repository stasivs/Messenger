import Messages


class Callback (Exception):
    def __init__(self, text="*not_defined*"):
        self.text = text

    def get_text(self):
        return self.text


class ServerError (Callback):
    pass


class CmdCallback (Callback):
    def get_message(self):
        return Messages.Info(self.text)


class CmdError (CmdCallback):
    def get_message(self):
        return Messages.Error(self.text)


class CmdAnswer (CmdCallback):
    def get_message(self):
        return Messages.CommandAnswer(self.text)


class CmdSyntaxError (CmdError):
    def __init__(self, command):
        text = "Syntax: /{} {}".format(
            command.name,
            command.syntax
        )
        super().__init__(text)


class CmdNotFound (CmdError):
    pass


class CmdNotPermissions (CmdError):
    pass
