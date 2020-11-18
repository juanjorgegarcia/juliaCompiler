from typing import List
from symbol_table import *
from compiler import Compiler
table = Symbol_Table()
compiler = Compiler()


class Node:

    i = 0

    def __init__(self, value: str, children):
        self.value = value
        self.children = children
        self.i = Node.newId()

    def Evaluate(self):
        pass

    @staticmethod
    def newId():
        Node.i += 1
        return Node.i


class BinOP(Node):
    def __init__(self, value: str, children=[None, None]):
        if children and len(children) == 2:
            super().__init__(value, children)
        else:
            raise SyntaxError(
                f"INVALID OPERATION: BinOP must have 2 children ")

    def Evaluate(self):

        if self.value == "+":
            self.children[0].Evaluate()
            compiler.write_line("PUSH EBX ;")
            self.children[1].Evaluate()
            compiler.write_line("POP EAX ;")
            compiler.write_line("ADD EAX, EBX ;")
            compiler.write_line("MOV EBX, EAX ;")

            # t1, v1 = self.children[0].Evaluate()
            # t2, v2 = self.children[1].Evaluate()

            # if(t1 == "String") or (t2 == "String"):
            #     raise SyntaxError(
            #         f"INVALID OPERATION: can't do arithmetics operation on strings")
            # return SymbolValue("Int", v1 + v2)

        elif self.value == "-":
            self.children[0].Evaluate()
            compiler.write_line("PUSH EBX ;")
            self.children[1].Evaluate()
            compiler.write_line("POP EAX ;")
            compiler.write_line("SUB EAX, EBX ;")
            compiler.write_line("MOV EBX, EAX ;")

            # t1, v1 = self.children[0].Evaluate()
            # t2, v2 = self.children[1].Evaluate()

            # if(t1 == "String") or (t2 == "String"):
            #     raise SyntaxError(
            #         f"INVALID OPERATION: can't do arithmetics operation on strings")
            # return SymbolValue("Int", int(v1 - v2))

        elif self.value == "*":
            self.children[0].Evaluate()
            compiler.write_line("PUSH EBX ;")
            self.children[1].Evaluate()
            compiler.write_line("POP EAX ;")
            compiler.write_line("MUL EBX ;")
            compiler.write_line("MOV EBX, EAX ;")

            # t1, v1 = self.children[0].Evaluate()
            # t2, v2 = self.children[1].Evaluate()

            # if(t1 == "String") or (t2 == "String"):
            #     v1, v2 = str(v1), str(v2)
            #     return SymbolValue("String", v1 + v2)

            # return SymbolValue("Int", int(v1 * v2))

        elif self.value == "/":
            self.children[0].Evaluate()
            compiler.write_line("PUSH EBX ;")
            self.children[1].Evaluate()
            compiler.write_line("POP EAX ;")
            compiler.write_line("DIV EBX ;")
            compiler.write_line("MOV EBX, EAX ;")

            # t1, v1 = self.children[0].Evaluate()
            # t2, v2 = self.children[1].Evaluate()

            # if(t1 == "String") or (t2 == "String"):
            #     raise SyntaxError(
            #         f"INVALID OPERATION: can't do arithmetics operation on strings")
            # return SymbolValue("Int", int(v1 / v2))

        elif self.value == "==":
            self.children[0].Evaluate()
            compiler.write_line("PUSH EBX ;")
            self.children[1].Evaluate()
            compiler.write_line("POP EAX ;")
            compiler.write_line("CMP EAX, EBX;")
            compiler.write_line("CALL binop_je")
            # return SymbolValue("Bool", bool(self.children[0].Evaluate().value == self.children[1].Evaluate().value))

        elif self.value == ">":
            # return SymbolValue("Bool", bool(self.children[0].Evaluate().value > self.children[1].Evaluate().value))
            self.children[0].Evaluate()
            compiler.write_line("PUSH EBX ;")
            self.children[1].Evaluate()
            compiler.write_line("POP EAX ;")
            compiler.write_line("CMP EAX, EBX;")
            compiler.write_line("CALL binop_jg")

        elif self.value == "<":
            # return SymbolValue("Bool", bool(self.children[0].Evaluate().value < self.children[1].Evaluate().value))
            self.children[0].Evaluate()
            compiler.write_line("PUSH EBX ;")
            self.children[1].Evaluate()
            compiler.write_line("POP EAX ;")
            compiler.write_line("CMP EAX, EBX;")
            compiler.write_line("CALL binop_jl")

        elif self.value == "&&":
            self.children[0].Evaluate()
            compiler.write_line("PUSH EBX ;")
            self.children[1].Evaluate()
            compiler.write_line("POP EAX ;")
            compiler.write_line("AND EAX, EBX ;")
            compiler.write_line("MOV EBX, EAX ;")

            # t1, v1 = self.children[0].Evaluate()
            # t2, v2 = self.children[1].Evaluate()

            # if(t1 == "String") or (t2 == "String"):
            #     raise SyntaxError(
            #         f"INVALID OPERATION: can't do boolean operation on strings")
            # return SymbolValue("Bool", bool(v1 and v2))

        elif self.value == "||":
            self.children[0].Evaluate()
            compiler.write_line("PUSH EBX ;")
            self.children[1].Evaluate()
            compiler.write_line("POP EAX ;")
            compiler.write_line("OR EAX, EBX ;")
            compiler.write_line("MOV EBX, EAX ;")

            # t1, v1 = self.children[0].Evaluate()
            # t2, v2 = self.children[1].Evaluate()

            # if(t1 == "String") or (t2 == "String"):
            #     raise SyntaxError(
            #         f"INVALID OPERATION: can't do boolean operation on strings")
            # return SymbolValue("Bool", bool(v1 or v2))


class UnOp(Node):
    def __init__(self, value: str, children=[None]):
        if children and len(children) == 1:
            super().__init__(value, children)
        else:
            raise SyntaxError(
                f"INVALID OPERATION: UnOp must have 1 children ")

    def Evaluate(self):
        if self.value == "+":
            self.children[0].Evaluate()
            compiler.write_line("MOV EBX, EAX;")

            # return SymbolValue("Int", self.children[0].Evaluate().value)
        if self.value == "-":
            self.children[0].Evaluate()
            compiler.write_line("IMUL -1;")
            compiler.write_line("MOV EBX, EAX;")

            # return SymbolValue("Int", -self.children[0].Evaluate().value)
        if self.value == "!":
            self.children[0].Evaluate()
            compiler.write_line("NOT EAX;")
            compiler.write_line("MOV EBX, EAX;")
            # return SymbolValue("Bool", not(self.children[0].Evaluate().value))


class IntVal(Node):
    def __init__(self, value: str):
        super().__init__(int(value), None)

    def Evaluate(self):
        compiler.write_line(f"MOV EBX, {self.value} ; ")
        # return SymbolValue("Int", self.value, 0)


class NoOP(Node):
    def __init__(self, value: str):
        super().__init__(value, None)

    def Evaluate(self):
        compiler.write_line("NOP")


class Assignment(Node):
    def __init__(self, value: str, children):
        if children and len(children) == 2:
            super().__init__(value, children)
        else:
            raise SyntaxError(
                f"INVALID OPERATION: Assigment must have 2 children ")

    def Evaluate(self):
        self.children[1].Evaluate()
        pos = table.get(self.children[0].value).pos
        compiler.write_line(f"MOV [EBP - {pos}], EBX;")
        # table.set_symbol(self.children[0].value, self.children[1].Evaluate())


class Identifier(Node):
    def __init__(self, value: str):
        super().__init__(value, [])

    def Evaluate(self):
        _type, _value, pos = table.get(self.value)
        compiler.write_line(f"MOV EBX, [EBP - {pos}];")
        # return table.get(self.value)


class Print(Node):
    def __init__(self, value: str, children=[None]):
        if children and len(children) == 1:
            super().__init__(value, children)
        else:
            raise SyntaxError(
                f"INVALID OPERATION: Print must have 1 child ")

    def Evaluate(self):
        if self.children:
            # print(self.children[0].Evaluate().value)
            self.children[0].Evaluate()

        compiler.write_line("PUSH EBX ;")
        compiler.write_line("CALL print ;")
        compiler.write_line("POP EBX ;")


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
        # while self.children[0].Evaluate().value:
        #     self.children[1].Evaluate()
        compiler.write_line(f"LOOP_{self.i}:;")
        self.children[0].Evaluate()
        compiler.write_line("CMP EBX, False ;")
        compiler.write_line(f"JE EXIT_{self.i} ;")
        self.children[1].Evaluate()
        compiler.write_line(f"JMP LOOP_{self.i} ;")
        compiler.write_line(f"EXIT_{self.i}: ;")


class IF(Node):
    def __init__(self, value: str, children):
        if children and len(children) >= 2:
            super().__init__(value, children)
        else:
            raise SyntaxError(
                f"INVALID OPERATION: IF must have 2 or 3 children ")

    def Evaluate(self):
        # if self.children[0].Evaluate().value:
        #     self.children[1].Evaluate()
        # else:
        #     if len(self.children) > 2 and self.children[2]:
        #         self.children[2].Evaluate()

        self.children[0].Evaluate()
        compiler.write_line("CMP EBX, False")
        compiler.write_line(f"JE EXIT_{self.i}")
        self.children[1].Evaluate()
        compiler.write_line(f"EXIT_{self.i}:")
        if(self.children[2]):
            self.children[0].Evaluate()
            compiler.write_line("CMP EBX, False")
            compiler.write_line(f"JNE EXIT_ELSE{self.i}")
            self.children[2].Evaluate()
            compiler.write_line(f"EXIT_ELSE{self.i}:")


class BoolVal(Node):
    def __init__(self, value: str):
        super().__init__(value, None)

    def Evaluate(self):
        # return SymbolValue("Bool", self.value)
        if self.value == True:
            compiler.write_line("CALL binop_true")
        elif self.value == False:
            compiler.write_line("CALL binop_false")


# class StringVal(Node):
#     def __init__(self, value: str):
#         super().__init__(value, None)

#     def Evaluate(self):
#         # if self.value == "True":
#         #     compiler.write_line("binop_true")
#         # elif self.value == "False":
#         #     compiler.write_line("binop_false")

#         return SymbolValue("String", self.value)


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
            compiler.write_line("PUSH DWORD 0 ;")
            table.declare_symbol(
                self.children[0].value, self.children[1].Evaluate())
        else:
            raise SyntaxError(
                f"INVALID OPERATION: node VarDec must have exactly 2 child ")


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
