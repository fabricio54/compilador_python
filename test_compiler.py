import sys
from antlr4 import *
from CalculatorLexer import CalculatorLexer
from CalculatorParser import CalculatorParser
from CalculatorVisitorImpl import EvalVisitor

def main():
    input_lines = []
    print("Digite suas expressões (linha vazia para terminar):")
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "":
            break
        input_lines.append(line)

    input_text = "\n".join(input_lines)
    input_stream = InputStream(input_text)
    lexer = CalculatorLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CalculatorParser(stream)
    tree = parser.prog()

    visitor = EvalVisitor()
    results = visitor.visit(tree)
    print("Variáveis:", visitor.variables)
    for result in results:
        if result is not None:
            print("Resultado:", result)

if __name__ == '__main__':
    main()
