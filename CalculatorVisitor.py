# Generated from Calculator.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete generic visitor for a parse tree produced by CalculatorParser.

class CalculatorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculatorParser#prog.
    def visitProg(self, ctx:CalculatorParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#stat.
    def visitStat(self, ctx:CalculatorParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#letDecl.
    def visitLetDecl(self, ctx:CalculatorParser.LetDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#expr.
    def visitExpr(self, ctx:CalculatorParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#condExpr.
    def visitCondExpr(self, ctx:CalculatorParser.CondExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#relOp.
    def visitRelOp(self, ctx:CalculatorParser.RelOpContext):
        return self.visitChildren(ctx)



del CalculatorParser