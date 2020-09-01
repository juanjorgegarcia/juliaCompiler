from _token import Token


class Tokenizer:

    def __init__(self, origin):
        self.origin = origin
        self.position = 0
        self.actual = None

    def selectNext(self):
        self.actual = Token("", "")

        if self.position == len(self.origin):
            self.actual = Token("EOF", "")
            return

        value = self.origin[self.position]

        if value == " ":
            self.actual = Token("SPACE", " ")
            self.position += 1
            self.selectNext()
            return

        if value == "+":
            self.actual = Token("PLUS", self.origin[self.position])
            self.position += 1
            return

        if value == "-":
            self.actual = Token("MINUS", self.origin[self.position])
            self.position += 1
            return

        if value.isnumeric():
            self.actual = Token("INT", '')

        for c in self.origin[self.position:]:
            if c.isnumeric():
                self.actual.value += c
                self.position += 1
            else:
                return
