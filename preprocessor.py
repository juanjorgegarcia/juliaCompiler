import re

class PreProcessor:
    code = None

    @staticmethod
    def process(code):
        processed = ""
        processed= re.sub(r"(#=)((.|\n)*?)(=#)", '', code)
        return processed
