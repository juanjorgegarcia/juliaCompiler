from collections import namedtuple

SymbolValue = namedtuple("SymbolValue", "type, value")


class Symbol_Table:
    def __init__(self):
        self.symbols = {}

    def get(self, symbol):
        if symbol in self.symbols:
            return self.symbols[symbol].value
        else:
            raise ValueError(
                f"INVALID ACCESS: there is no symbol: {symbol} in the Symbol Table{self.symbols}")

    def set_symbol(self, symbol, value):
        if symbol in self.symbols:
            self.symbols[symbol] = SymbolValue(
                self.symbols[symbol].type, value)
        else:
            raise ValueError(
                f"INVALID ASSIGNMENT: variable {symbol} is NOT declared in the Symbol Table {self.symbols}")

    def declare_symbol(self, symbol, _type):
        if symbol not in self.symbols:
            self.symbols[symbol] = SymbolValue(_type, None)
        else:
            raise ValueError(
                f"INVALID DECLARATION: variable {symbol} already declared in the Symbol Table{self.symbols}")
