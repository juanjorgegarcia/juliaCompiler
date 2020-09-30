from _parser import Parser
import sys

with open(sys.argv[1], 'r') as f:
    output = f.read()

Parser.run(output).Evaluate()
