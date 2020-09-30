from tokenizer import Tokenizer
from preprocessor import PrePro
from node import *


class Parser:
    tokens = None

    @staticmethod
    def run(code):
        processed_code = PrePro.filter(code)
        Parser.tokens = Tokenizer(processed_code)
        Parser.tokens.selectNext()
        res = Parser.parseBlock()
        if Parser.tokens.actual._type == "EOF":
            return res
        else:
            raise SyntaxError(
                f"INVALID TOKEN: token type espected {'EOF'}, instead got {Parser.tokens.actual.value} in position: ({Parser.tokens.position})")

    @staticmethod
    def parseExpression():
        res = Parser.parseTerm()
        while (Parser.tokens.actual._type == 'PLUS' or Parser.tokens.actual._type == 'MINUS'):
            if Parser.tokens.actual._type == 'PLUS' or Parser.tokens.actual._type == 'MINUS':
                res = BinOP(Parser.tokens.actual.value,
                            [res, None])
                Parser.tokens.selectNext()
                res.children[1] = Parser.parseTerm()

            else:
                raise SyntaxError(
                    f"INVALID TOKEN: unknown token found: {Parser.tokens.actual.value} in position: ({Parser.tokens.position})")
        return res

    @staticmethod
    def parseTerm():
        res = Parser.parseFactor()

        while (Parser.tokens.actual._type == 'DIV' or Parser.tokens.actual._type == 'MULT'):
            if Parser.tokens.actual._type == 'DIV' or Parser.tokens.actual._type == 'MULT':
                res = BinOP(Parser.tokens.actual.value,
                            [res, None])

                Parser.tokens.selectNext()
                res.children[1] = Parser.parseFactor()

            else:
                raise SyntaxError(
                    f"INVALID TOKEN: unknown token found: {Parser.tokens.actual.value} in position: ({Parser.tokens.position})")
        return res

    @staticmethod
    def parseFactor():

        if Parser.tokens.actual._type == 'INT':
            res = IntVal(Parser.tokens.actual.value)
            Parser.tokens.selectNext()

        elif Parser.tokens.actual._type == 'PLUS' or Parser.tokens.actual._type == 'MINUS':
            res = UnOp(Parser.tokens.actual.value, [None])
            Parser.tokens.selectNext()
            res.children[0] = Parser.parseFactor()

        elif Parser.tokens.actual._type == "OPEN_PARENTHESIS":
            Parser.tokens.selectNext()
            res = Parser.parseExpression()

            if Parser.tokens.actual._type == "CLOSED_PARENTHESIS":
                Parser.tokens.selectNext()
            else:
                raise SyntaxError(
                    f'INVALID SYNTAX: missing "CLOSED_PARENTHESIS"({Parser.tokens.actual.value}) in position: ({Parser.tokens.position}, parenthesis are opened but no closed)')
        elif Parser.tokens.actual._type == "INDENTIFIER":
            res = Indentifier(Parser.tokens.actual.value)
            Parser.tokens.selectNext()
        else:
            raise SyntaxError(
                f"INVALID TOKEN: token type espected {' (INT) or (PLUS) or (MINUS) or (OPEN_PARENTHESIS) or (CLOSED_PARENTHESIS) '}, instead got {Parser.tokens.actual.value} in position: ({Parser.tokens.position})")
        return res

    @staticmethod
    def parseBlock():
        stmt = Statment()
        while (Parser.tokens.actual._type != 'EOF'):
            stmt.children.append(Parser.parseCommand())

        return stmt

    @staticmethod
    def parseCommand():
        res = None
        if Parser.tokens.actual._type == "INDENTIFIER":

            res = Parser.tokens.actual
            Parser.tokens.selectNext()
            if Parser.tokens.actual._type == "EQUAL":
                res = Assignment(Parser.tokens.actual.value, [res, None])
                Parser.tokens.selectNext()
                res.children[1] = Parser.parseExpression()

        elif Parser.tokens.actual._type == "PRINT":
            Parser.tokens.selectNext()
            if Parser.tokens.actual._type == "OPEN_PARENTHESIS":
                Parser.tokens.selectNext()
                res = Print(Parser.tokens.actual.value, [Parser.parseExpression()
                                                         ])

                if Parser.tokens.actual._type == "CLOSED_PARENTHESIS":
                    Parser.tokens.selectNext()
                else:
                    raise SyntaxError(
                        f'INVALID SYNTAX: missing "CLOSED_PARENTHESIS"({Parser.tokens.actual.value}) in position: ({Parser.tokens.position}, parenthesis are opened but no closed)')
            else:
                raise SyntaxError(
                    f'INVALID SYNTAX: missing "OPEN_PARENTHESIS" after println call, instead got ({Parser.tokens.actual.value}) in position: ({Parser.tokens.position})')
        if Parser.tokens.actual._type == "NEW_LINE":
            Parser.tokens.selectNext()
            if res:
                return res
            else:
                NoOP(Parser.tokens.actual.value)
                return res
