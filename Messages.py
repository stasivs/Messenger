from datetime import datetime


class BlankMessage:
    def __init__(self, text):
        self.__text = text

    def get_message(self):
        return self.__text


class UserMessage (BlankMessage):
    def __init__(self, text):
        super().__init__(text)
        self.owner_nick = "*not_defined*"

    def get_message(self):
        return "[{}] {} -> {}".format(
            datetime.strftime(datetime.now(), "[%d.%m %H:%M]"),
            self.owner_nick,
            self.__text
        )


class Info (BlankMessage):
    def __init__(self, text):
        super().__init__(text)

    def get_message(self):
        return "INFO: {}".format(
            self.__text
        )


class Error(BlankMessage):
    def __init__(self, text):
        super().__init__(text)

    def get_message(self):
        return "ERROR: {}".format(
            self.__text
        )


class BCast(BlankMessage):
    def __init__(self, text):
        super().__init__(text)

    def get_message(self):
        return "BCAST: {}".format(
            self.__text
        )
