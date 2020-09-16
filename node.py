from typing import List


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
            return int(self.children[0].Evaluate() / self.children[1].Evaluate())


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
