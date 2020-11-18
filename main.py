from _parser import Parser
from node import compiler
import sys

with open(sys.argv[1], 'r') as f:
    output = f.read()

Parser.run(output).Evaluate()
compiler.write_file()
