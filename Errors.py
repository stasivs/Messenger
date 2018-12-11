from Messages import *


class CmdCallback (Exception):
    Message_Type = Info

    def __init__(self, text):
        self.__text = text

    def get_message(self):
        return CmdCallback.Message_Type(self.__text)


class CmdError (CmdCallback):
    Message_Type = Error


class CmdBroadcast (CmdCallback):
    Message_Type = Bcast


class ServerError (Exception):
    def __init__(self, text="*not_defined*"):
        self.__text = text

    def get_error(self):
        return self.__text

    def formatted(self, *args):
        return ServerError(self.__text.format(
            *args
        ))
