class Symbol_Table:
    def __init__(self):
        self.symbols = {}

    def get(self, symbol):
        if symbol in self.symbols:
            return self.symbols[symbol]
        else:
            raise ValueError(
                f"INVALID ACCESS: there is no symbol: {symbol} in the Symbol Table{self.symbols}")

    def set_symbol(self, symbol, value):
        self.symbols[symbol] = value
