from tokenizer import Tokenizer
from preprocessor import PrePro


class Parser:
    tokens = None

    @staticmethod
    def run(code):
        processed_code = PrePro.filter(code)
        Parser.tokens = Tokenizer(processed_code)
        Parser.tokens.selectNext()
        res = Parser.parseExpression()
        if Parser.tokens.actual._type == "EOF":
            return res
        else:
            raise SyntaxError(
                f"INVALID TOKEN: token type espected {'EOF'}, instead got {Parser.tokens.actual.value} in position: ({Parser.tokens.position})")

    @staticmethod
    def parseTerm():
        res = Parser.parseFactor()

        while (Parser.tokens.actual._type == 'DIV' or Parser.tokens.actual._type == 'MULT'):
            if Parser.tokens.actual._type == 'DIV':
                Parser.tokens.selectNext()
                res /= Parser.parseFactor()

            elif Parser.tokens.actual._type == 'MULT':
                Parser.tokens.selectNext()
                res *= Parser.parseFactor()
            else:
                raise SyntaxError(
                    f"INVALID TOKEN: unknown token found: {Parser.tokens.actual.value} in position: ({Parser.tokens.position})")
        return int(res)

    @staticmethod
    def parseFactor():

        res = 0
        if Parser.tokens.actual._type == 'INT':
            res += int(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
        elif Parser.tokens.actual._type == 'PLUS':
            Parser.tokens.selectNext()
            res += Parser.parseFactor()

        elif Parser.tokens.actual._type == 'MINUS':
            Parser.tokens.selectNext()
            res -= Parser.parseFactor()

        elif Parser.tokens.actual._type == "OPEN_PARENTHESIS":
            Parser.tokens.selectNext()
            res = Parser.parseExpression()

            if Parser.tokens.actual._type == "CLOSED_PARENTHESIS":
                Parser.tokens.selectNext()
            else:
                raise SyntaxError(
                    f'INVALID SYNTAX: missing "CLOSED_PARENTHESIS"({Parser.tokens.actual.value}) in position: ({Parser.tokens.position}, parenthesis are opened but no closed)')
        else:
            raise SyntaxError(
                f"INVALID TOKEN: token type espected {' (INT) or (PLUS) or (MINUS) or (OPEN_PARENTHESIS) or (CLOSED_PARENTHESIS) '}, instead got {Parser.tokens.actual.value} in position: ({Parser.tokens.position})")
        return int(res)

    @staticmethod
    def parseExpression():
        res = Parser.parseTerm()
        while (Parser.tokens.actual._type == 'PLUS' or Parser.tokens.actual._type == 'MINUS'):
            if Parser.tokens.actual._type == 'PLUS':
                Parser.tokens.selectNext()
                res += Parser.parseTerm()

            elif Parser.tokens.actual._type == 'MINUS':
                Parser.tokens.selectNext()
                res -= Parser.parseTerm()
            else:
                raise SyntaxError(
                    f"INVALID TOKEN: unknown token found: {Parser.tokens.actual.value} in position: ({Parser.tokens.position})")
        return int(res)
