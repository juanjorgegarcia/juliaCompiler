from collections import namedtuple

SymbolValue = namedtuple("SymbolValue", "type, value, pos")


class Symbol_Table:
    def __init__(self):
        self.symbols = {}
        self.pos = 0

    def get(self, symbol):
        if symbol in self.symbols:
            return self.symbols[symbol]
        else:
            raise ValueError(
                f"INVALID ACCESS: there is no symbol: {symbol} in the Symbol Table{self.symbols}")

    def set_symbol(self, symbol, new_var):
        new_type, new_value = new_var
        if symbol in self.symbols:
            __, _type, _pos = self.symbols[symbol]

            if self.check_types(new_value, _type) and new_type == _type:

                self.symbols[symbol] = SymbolValue(
                    _type, new_value, _pos)
            else:
                raise ValueError(
                    f"INVALID ASSIGNMENT: can't assign value {new_value} to variable of type {_type} ")

        else:
            raise ValueError(
                f"INVALID ASSIGNMENT: variable {symbol} is NOT declared in the Symbol Table {self.symbols}")

    def declare_symbol(self, symbol, _type):
        if symbol not in self.symbols:
            self.pos += 4
            self.symbols[symbol] = SymbolValue(_type, None, self.pos)
        else:
            raise ValueError(
                f"INVALID DECLARATION: variable {symbol} already declared in the Symbol Table{self.symbols}")

    def check_types(self, value, _type):
        if _type == "Bool":
            return self.is_boolean(value)
        elif _type == "Int":
            return self.is_int(value)
        elif _type == "String":
            return self.is_str(value)

    def is_boolean(self, value):
        if value == True or value == False:
            return True
        else:
            return False

    def is_int(self, value):
        if isinstance(value, int):
            return True
        else:
            return False

    def is_str(self, value):
        if isinstance(value, str):
            return True
        else:
            return False
