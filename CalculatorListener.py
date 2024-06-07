# Generated from Calculator.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete listener for a parse tree produced by CalculatorParser.
class CalculatorListener(ParseTreeListener):

    # Enter a parse tree produced by CalculatorParser#prog.
    def enterProg(self, ctx:CalculatorParser.ProgContext):
        pass

    # Exit a parse tree produced by CalculatorParser#prog.
    def exitProg(self, ctx:CalculatorParser.ProgContext):
        pass


    # Enter a parse tree produced by CalculatorParser#stat.
    def enterStat(self, ctx:CalculatorParser.StatContext):
        pass

    # Exit a parse tree produced by CalculatorParser#stat.
    def exitStat(self, ctx:CalculatorParser.StatContext):
        pass


    # Enter a parse tree produced by CalculatorParser#letDecl.
    def enterLetDecl(self, ctx:CalculatorParser.LetDeclContext):
        pass

    # Exit a parse tree produced by CalculatorParser#letDecl.
    def exitLetDecl(self, ctx:CalculatorParser.LetDeclContext):
        pass


    # Enter a parse tree produced by CalculatorParser#expr.
    def enterExpr(self, ctx:CalculatorParser.ExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#expr.
    def exitExpr(self, ctx:CalculatorParser.ExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#condExpr.
    def enterCondExpr(self, ctx:CalculatorParser.CondExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#condExpr.
    def exitCondExpr(self, ctx:CalculatorParser.CondExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#relOp.
    def enterRelOp(self, ctx:CalculatorParser.RelOpContext):
        pass

    # Exit a parse tree produced by CalculatorParser#relOp.
    def exitRelOp(self, ctx:CalculatorParser.RelOpContext):
        pass



del CalculatorParser