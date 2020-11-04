from typing import List
from symbol_table import *
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
            t1, v1 = self.children[0].Evaluate()
            t2, v2 = self.children[1].Evaluate()

            if(t1 == "String") or (t2 == "String"):
                raise SyntaxError(
                    f"INVALID OPERATION: can't do arithmetics operation on strings")
            return SymbolValue("Int", v1 + v2)

        elif self.value == "-":
            t1, v1 = self.children[0].Evaluate()
            t2, v2 = self.children[1].Evaluate()

            if(t1 == "String") or (t2 == "String"):
                raise SyntaxError(
                    f"INVALID OPERATION: can't do arithmetics operation on strings")
            return SymbolValue("Int", int(v1 - v2))

        elif self.value == "*":
            t1, v1 = self.children[0].Evaluate()
            t2, v2 = self.children[1].Evaluate()

            if(t1 == "String") or (t2 == "String"):
                v1, v2 = str(v1), str(v2)
                return SymbolValue("String", v1 + v2)

            return SymbolValue("Int", int(v1 * v2))

        elif self.value == "/":
            t1, v1 = self.children[0].Evaluate()
            t2, v2 = self.children[1].Evaluate()

            if(t1 == "String") or (t2 == "String"):
                raise SyntaxError(
                    f"INVALID OPERATION: can't do arithmetics operation on strings")
            return SymbolValue("Int", int(v1 / v2))

        elif self.value == "==":
            return SymbolValue("Bool", bool(self.children[0].Evaluate().value == self.children[1].Evaluate().value))

        elif self.value == ">":
            return SymbolValue("Bool", bool(self.children[0].Evaluate().value > self.children[1].Evaluate().value))

        elif self.value == "<":
            return SymbolValue("Bool", bool(self.children[0].Evaluate().value < self.children[1].Evaluate().value))

        elif self.value == "&&":
            t1, v1 = self.children[0].Evaluate()
            t2, v2 = self.children[1].Evaluate()

            if(t1 == "String") or (t2 == "String"):
                raise SyntaxError(
                    f"INVALID OPERATION: can't do boolean operation on strings")
            return SymbolValue("Bool", bool(v1 and v2))

        elif self.value == "||":
            t1, v1 = self.children[0].Evaluate()
            t2, v2 = self.children[1].Evaluate()

            if(t1 == "String") or (t2 == "String"):
                raise SyntaxError(
                    f"INVALID OPERATION: can't do boolean operation on strings")
            return SymbolValue("Bool", bool(v1 or v2))


class UnOp(Node):
    def __init__(self, value: str, children=[None]):
        if children and len(children) == 1:
            super().__init__(value, children)
        else:
            raise SyntaxError(
                f"INVALID OPERATION: UnOp must have 1 children ")

    def Evaluate(self):
        if self.value == "+":
            return SymbolValue("Int", self.children[0].Evaluate().value)
        if self.value == "-":
            return SymbolValue("Int", -self.children[0].Evaluate().value)
        if self.value == "!":
            return SymbolValue("Bool", not(self.children[0].Evaluate().value))


class IntVal(Node):
    def __init__(self, value: str):
        super().__init__(int(value), None)

    def Evaluate(self):
        return SymbolValue("Int", self.value)


class NoOP(Node):
    def __init__(self, value: str):
        super().__init__(value, None)

    def Evaluate(self):
        pass


class Assignment(Node):
    def __init__(self, value: str, children):
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
        # _type, _value = table.get(self.value)
        return table.get(self.value)


class Print(Node):
    def __init__(self, value: str, children=[None]):
        if children and len(children) == 1:
            super().__init__(value, children)
        else:
            raise SyntaxError(
                f"INVALID OPERATION: Print must have 1 child ")

    def Evaluate(self):
        if self.children:
            print(self.children[0].Evaluate().value)


class Statement(Node):
    def __init__(self, children):
        super().__init__("", [])

    def Evaluate(self):
        for child in self.children:
            child.Evaluate()


class Readline(Node):
    def __init__(self):
        super().__init__("", None)

    def Evaluate(self):
        self.value = int(input())
        return SymbolValue("Int", self.value)


class While(Node):
    def __init__(self, value: str, children=[None, None]):
        if children and len(children) == 2:
            super().__init__(value, children)
        else:
            raise SyntaxError(
                f"INVALID OPERATION: WHILE must have 2 children ")

    def Evaluate(self):
        while self.children[0].Evaluate().value:
            self.children[1].Evaluate()


class IF(Node):
    def __init__(self, value: str, children):
        if children and len(children) >= 2:
            super().__init__(value, children)
        else:
            raise SyntaxError(
                f"INVALID OPERATION: IF must have 2 or 3 children ")

    def Evaluate(self):
        if self.children[0].Evaluate().value:
            self.children[1].Evaluate()
        else:
            if len(self.children) > 2 and self.children[2]:
                self.children[2].Evaluate()


class BoolVal(Node):
    def __init__(self, value: str):
        super().__init__(value, None)

    def Evaluate(self):
        return SymbolValue("Bool", self.value)


class StringVal(Node):
    def __init__(self, value: str):
        super().__init__(value, None)

    def Evaluate(self):
        return SymbolValue("String", self.value)


class VarDec(Node):
    # value = None, children[0] = identifier_value (node: Identifier), children[1] = variable type (node: VarType)
    def __init__(self, value: str, children):
        if children and len(children) == 2:
            super().__init__(value, children)
        else:
            raise SyntaxError(
                f"INVALID OPERATION: node VarDec must have exactly 2 children ")

    def Evaluate(self):
        if self.children and len(self.children) == 2:
            table.declare_symbol(
                self.children[0].value, self.children[1].Evaluate())
        else:
            raise SyntaxError(
                f"INVALID OPERATION: node VarDec must have exactly 1 child ")


class VarType(Node):
    def __init__(self, value: str):  # value = variable type
        if value:
            self.value = value
        else:
            raise SyntaxError(
                f"INVALID OPERATION: node VarType must have a value ")

    def Evaluate(self):
        if self.value:
            return self.value
        else:
            raise SyntaxError(
                f"INVALID OPERATION: node VarType must have a value ")
