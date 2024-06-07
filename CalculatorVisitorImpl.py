from CalculatorParser import CalculatorParser
from CalculatorVisitor import CalculatorVisitor

class EvalVisitor(CalculatorVisitor):
    def __init__(self):
        self.variables = {}

    def visitProg(self, ctx:CalculatorParser.ProgContext):
        results = []
        for child in ctx.stat():
            result = self.visit(child)
            if result is not None:
                results.append(result)
        return results

    def visitLetDecl(self, ctx:CalculatorParser.LetDeclContext):
        for i in range(len(ctx.ID())):
            var_name = ctx.ID(i).getText()
            var_value = self.visit(ctx.expr(i))
            self.variables[var_name] = var_value
        return None

    def visitExpr(self, ctx:CalculatorParser.ExprContext):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.ID():
            var_name = ctx.ID().getText()
            if var_name not in self.variables:
                raise Exception(f"Error: Variable '{var_name}' not declared.")
            return self.variables[var_name]
        elif ctx.getChildCount() == 3 and ctx.getChild(1).getText() in ['+', '-', '*', '/', '>', '<', '==', '!=', '>=', '<=']:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            if left is None or right is None:
                raise Exception("Error: One of the operands is None.")
            op = ctx.getChild(1).getText()
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                return left / right
            elif op == '>':
                return left > right
            elif op == '<':
                return left < right
            elif op == '==':
                return left == right
            elif op == '!=':
                return left != right
            elif op == '>=':
                return left >= right
            elif op == '<=':
                return left <= right
        elif ctx.condExpr():
            return self.visit(ctx.condExpr())
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.expr(0))
        return None

    def visitCondExpr(self, ctx:CalculatorParser.CondExprContext):
        cond = self.visit(ctx.expr(0))
        if cond:
            return self.visit(ctx.expr(1))
        else:
            return self.visit(ctx.expr(2))

    def visitRelOp(self, ctx:CalculatorParser.RelOpContext):
        return self.visitChildren(ctx)
