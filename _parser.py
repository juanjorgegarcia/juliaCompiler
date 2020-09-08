from tokenizer import Tokenizer
from preprocessor import PrePro


class Parser:
    tokens = None

    @staticmethod
    def run(code):
        processed_code = PrePro.filter(code)
        Parser.tokens = Tokenizer(processed_code)
        res = Parser.parseExpression()
        if Parser.tokens.actual._type == "EOF":
            return res
        else:
            raise SyntaxError(
                f"INVALID TOKEN: token type espected {'EOF'}, instead got {Parser.tokens.actual.value} in position: ({Parser.tokens.position})")

    @staticmethod
    def parseTerm():
        Parser.tokens.selectNext()

        if Parser.tokens.actual._type == 'INT':
            res = int(Parser.tokens.actual.value)

            Parser.tokens.selectNext()

            while Parser.tokens.actual._type == 'DIV' or Parser.tokens.actual._type == 'MULT':
                if Parser.tokens.actual._type == 'DIV':
                    Parser.tokens.selectNext()

                    if Parser.tokens.actual._type == 'INT':
                        res /= int(Parser.tokens.actual.value)
                    else:
                        raise SyntaxError(
                            f"INVALID TOKEN: token type espected {'INT'}, instead got {Parser.tokens.actual._type} in position: ({Parser.tokens.position}) ")
                if Parser.tokens.actual._type == 'MULT':
                    Parser.tokens.selectNext()

                    if Parser.tokens.actual._type == 'INT':
                        res *= int(Parser.tokens.actual.value)
                    else:
                        raise SyntaxError(
                            f"INVALID TOKEN: token type espected {'INT'}, instead got {Parser.tokens.actual._type} in position: ({Parser.tokens.position})")
                Parser.tokens.selectNext()
            return int(res)

        else:
            raise SyntaxError(
                f'INVALID TOKEN: ({Parser.tokens.actual.value}) in position: ({Parser.tokens.position})')

    @staticmethod
    def parseExpression():

        res = Parser.parseTerm()
        # Parser.tokens.selectNext()

        while (Parser.tokens.actual._type == 'PLUS' or Parser.tokens.actual._type == 'MINUS') and Parser.tokens.actual._type != 'EOF':
            if Parser.tokens.actual._type == 'PLUS':
                res += Parser.parseTerm()

            if Parser.tokens.actual._type == 'MINUS':
                res -= Parser.parseTerm()
        return res
