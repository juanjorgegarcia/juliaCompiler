from typing import List
from symbol_table import Symbol_Table
table = Symbol_Table()


class Node:
    def __init__(self, value: str, children):
        self.value = value
        self.children = children

    def Evaluate(self):
        pass


class BinOP(Node):
    def __init__(self, value: str, children=[None, None]):
        if children and len(children) == 2:
            super().__init__(value, children)
        else:
            raise SyntaxError(
                f"INVALID OPERATION: BinOP must have 2 children ")

    def Evaluate(self):
        if self.value == "+":
            return self.children[0].Evaluate() + self.children[1].Evaluate()
        elif self.value == "-":
            return self.children[0].Evaluate() - self.children[1].Evaluate()
        elif self.value == "*":
            return self.children[0].Evaluate() * self.children[1].Evaluate()
        elif self.value == "/":
            return int(self.children[0].Evaluate() or self.children[1].Evaluate())
        elif self.value == "||":
            return (self.children[0].Evaluate() or self.children[1].Evaluate())
        elif self.value == "&&":
            return (self.children[0].Evaluate() and self.children[1].Evaluate())
        elif self.value == "==":
            return (self.children[0].Evaluate() == self.children[1].Evaluate())
        elif self.value == ">":
            return (self.children[0].Evaluate() > self.children[1].Evaluate())
        elif self.value == "<":
            return (self.children[0].Evaluate() < self.children[1].Evaluate())


class UnOp(Node):
    def __init__(self, value: str, children=[None]):
        if children and len(children) == 1:
            super().__init__(value, children)
        else:
            raise SyntaxError(
                f"INVALID OPERATION: UnOp must have 1 children ")

    def Evaluate(self):
        if self.value == "+":
            return self.children[0].Evaluate()
        if self.value == "-":
            return -self.children[0].Evaluate()
        if self.value == "!":
            return not(self.children[0].Evaluate())


class IntVal(Node):
    def __init__(self, value: str):
        super().__init__(int(value), None)

    def Evaluate(self):
        return self.value


class NoOP(Node):
    def __init__(self, value: str):
        super().__init__(value, None)

    def Evaluate(self):
        pass


class Assignment(Node):
    def __init__(self, value: str, children=[None, None]):
        if children and len(children) == 2:
            super().__init__(value, children)
        else:
            raise SyntaxError(
                f"INVALID OPERATION: Assigment must have 2 children ")

    def Evaluate(self):
        table.set_symbol(self.children[0].value, self.children[1].Evaluate())


class Identifier(Node):
    def __init__(self, value: str):
        super().__init__(value, [])

    def Evaluate(self):
        return table.get(self.value)


class Print(Node):
    def __init__(self, value: str, children=[None]):
        if children and len(children) == 1:
            super().__init__(value, children)
        else:
            raise SyntaxError(
                f"INVALID OPERATION: Print must have 1 children ")

    def Evaluate(self):
        if self.children:
            print(self.children[0].Evaluate())
        return


class Statement(Node):
    def __init__(self, children=[]):
        super().__init__("", children)

    def Evaluate(self):
        for child in self.children:
            child.Evaluate()


class Readline(Node):
    def __init__(self):
        super().__init__("", None)

    def Evaluate(self):
        self.value = int(input())
        return self.value


class While(Node):
    def __init__(self, value: str, children=[None, None]):
        if children and len(children) == 2:
            super().__init__(value, children)
        else:
            raise SyntaxError(
                f"INVALID OPERATION: WHILE must have 2 children ")

    def Evaluate(self):
        while self.children[0].Evaluate():
            self.children[1].Evaluate()


class IF(Node):
    def __init__(self, value: str, children=[None, None, None]):
        if children and len(children) >= 2:
            super().__init__(value, children)
        else:
            raise SyntaxError(
                f"INVALID OPERATION: IF must have 2 or 3 children ")

    def Evaluate(self):
        res = 0
        if self.children[0].Evaluate():
            res = self.children[1].Evaluate()
        else:
            if self.children[2]:
                res = self.children[2].Evaluate()
        return res
