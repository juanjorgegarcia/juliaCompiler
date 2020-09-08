import re


class PrePro:
    code = None

    def filter(code):
        processed = ""
        processed = re.sub(r"(#=)((.|\n)*?)(=#)", '', code)
        return processed
