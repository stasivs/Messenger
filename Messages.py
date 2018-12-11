from datetime import datetime


class BlankMessage:
    def __init__(self, text):
        self.text = text

    def get_message(self):
        return self.text


class UserMessage (BlankMessage):
    def __init__(self, text, owner_nick):
        super().__init__(text)
        self.__owner_nick = owner_nick

    def get_message(self):
        return "{} {} -> {}".format(
            datetime.strftime(datetime.now(), "[%d.%m %H:%M]"),
            self.__owner_nick,
            self.text
        )


class Info (BlankMessage):
    def __init__(self, text):
        super().__init__(text)

    def get_message(self):
        return "INFO: {}".format(
            self.text
        )


class Error(BlankMessage):
    def __init__(self, text):
        super().__init__(text)

    def get_message(self):
        return "ERROR: {}".format(
            self.text
        )


class Bcast(BlankMessage):
    def __init__(self, text):
        super().__init__(text)

    def get_message(self):
        return "BCAST: {}".format(
            self.text
        )


class CommandAnswer (BlankMessage):
    def __init__(self, text):
        super().__init__(text)

    def get_message(self):
        return "{}".format(
            self.text
        )
