from _token import Token


class Tokenizer:

    def __init__(self, origin):
        self.origin = origin
        self.position = 0
        self.actual = None
        self.keywords = {"println": "PRINT"}

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

        if value == "/":
            self.actual = Token("DIV", value)
            self.position += 1
            return

        if value == "*":
            self.actual = Token("MULT", value)
            self.position += 1
            return

        if value == "+":
            self.actual = Token("PLUS", value)
            self.position += 1
            return

        if value == "-":
            self.actual = Token("MINUS", value)
            self.position += 1
            return

        if value == "(":
            self.actual = Token("OPEN_PARENTHESIS", value)
            self.position += 1
            return
        if value == ")":
            self.actual = Token("CLOSED_PARENTHESIS", value)
            self.position += 1
            return

        if value == "\n":
            self.actual = Token("NEW_LINE", '\n')
            self.position += 1
            return

        if value == "=":
            self.actual = Token("EQUAL", value)
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

        if value.isalpha():
            self.actual = Token("INDENTIFIER", '')
            for c in self.origin[self.position:]:
                if c.isalpha() or c.isnumeric() or c is "_":
                    self.actual.value += c
                    self.position += 1
                else:
                    break
            if self.actual.value in self.keywords:
                self.actual._type = self.keywords[self.actual.value]
            return
