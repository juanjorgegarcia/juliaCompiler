from tokenizer import Tokenizer


class Parser:
    tokens = None

    @staticmethod
    def run(code):
        Parser.tokens = Tokenizer(code)
        return Parser.parseExpression()

    @staticmethod
    def parseExpression():
        Parser.tokens.selectNext()

        if Parser.tokens.actual._type == 'INT':
            res = int(Parser.tokens.actual.value)

            Parser.tokens.selectNext()

            if Parser.tokens.actual._type == 'INT':
                raise NameError(
                    'INVALID GRAMMAR: Two Numbers separated only by spaces')
            while Parser.tokens.actual._type == 'PLUS' or Parser.tokens.actual._type == 'MINUS':
                if Parser.tokens.actual._type == 'PLUS':
                    Parser.tokens.selectNext()

                    if Parser.tokens.actual._type == 'INT':
                        res += int(Parser.tokens.actual.value)
                    else:
                        raise NameError('TOKEN INVALIDO')
                if Parser.tokens.actual._type == 'MINUS':
                    Parser.tokens.selectNext()

                    if Parser.tokens.actual._type == 'INT':
                        res -= int(Parser.tokens.actual.value)
                    else:
                        raise NameError('TOKEN INVALIDO')
                Parser.tokens.selectNext()
            return res
        else:
            raise NameError('TOKEN INVALIDO')
