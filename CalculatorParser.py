# Generated from Calculator.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,20,68,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,1,1,1,3,1,20,8,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,5,2,30,8,2,10,2,12,2,33,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,43,8,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,51,8,3,10,3,12,3,54,9,
        3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,0,1,6,6,0,
        2,4,6,8,10,0,3,1,0,4,5,1,0,6,7,1,0,12,17,69,0,13,1,0,0,0,2,19,1,
        0,0,0,4,21,1,0,0,0,6,42,1,0,0,0,8,55,1,0,0,0,10,65,1,0,0,0,12,14,
        3,2,1,0,13,12,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,
        16,1,1,0,0,0,17,20,3,4,2,0,18,20,3,6,3,0,19,17,1,0,0,0,19,18,1,0,
        0,0,20,3,1,0,0,0,21,22,5,1,0,0,22,23,5,18,0,0,23,24,5,2,0,0,24,31,
        3,6,3,0,25,26,5,3,0,0,26,27,5,18,0,0,27,28,5,2,0,0,28,30,3,6,3,0,
        29,25,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,5,1,0,
        0,0,33,31,1,0,0,0,34,35,6,3,-1,0,35,36,5,8,0,0,36,37,3,6,3,0,37,
        38,5,9,0,0,38,43,1,0,0,0,39,43,5,18,0,0,40,43,5,19,0,0,41,43,3,8,
        4,0,42,34,1,0,0,0,42,39,1,0,0,0,42,40,1,0,0,0,42,41,1,0,0,0,43,52,
        1,0,0,0,44,45,10,6,0,0,45,46,7,0,0,0,46,51,3,6,3,7,47,48,10,5,0,
        0,48,49,7,1,0,0,49,51,3,6,3,6,50,44,1,0,0,0,50,47,1,0,0,0,51,54,
        1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,7,1,0,0,0,54,52,1,0,0,0,55,
        56,5,8,0,0,56,57,3,6,3,0,57,58,3,10,5,0,58,59,3,6,3,0,59,60,5,9,
        0,0,60,61,5,10,0,0,61,62,3,6,3,0,62,63,5,11,0,0,63,64,3,6,3,0,64,
        9,1,0,0,0,65,66,7,2,0,0,66,11,1,0,0,0,6,15,19,31,42,50,52
    ]

class CalculatorParser ( Parser ):

    grammarFileName = "Calculator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'='", "','", "'*'", "'/'", "'+'", 
                     "'-'", "'('", "')'", "'?'", "':'", "'>'", "'<'", "'=='", 
                     "'>='", "'<='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_letDecl = 2
    RULE_expr = 3
    RULE_condExpr = 4
    RULE_relOp = 5

    ruleNames =  [ "prog", "stat", "letDecl", "expr", "condExpr", "relOp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    ID=18
    INT=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.StatContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.StatContext,i)


        def getRuleIndex(self):
            return CalculatorParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CalculatorParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.stat()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 786690) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def letDecl(self):
            return self.getTypedRuleContext(CalculatorParser.LetDeclContext,0)


        def expr(self):
            return self.getTypedRuleContext(CalculatorParser.ExprContext,0)


        def getRuleIndex(self):
            return CalculatorParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = CalculatorParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.letDecl()
                pass
            elif token in [8, 18, 19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CalculatorParser.ID)
            else:
                return self.getToken(CalculatorParser.ID, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.ExprContext,i)


        def getRuleIndex(self):
            return CalculatorParser.RULE_letDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetDecl" ):
                listener.enterLetDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetDecl" ):
                listener.exitLetDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetDecl" ):
                return visitor.visitLetDecl(self)
            else:
                return visitor.visitChildren(self)




    def letDecl(self):

        localctx = CalculatorParser.LetDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_letDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(CalculatorParser.T__0)
            self.state = 22
            self.match(CalculatorParser.ID)
            self.state = 23
            self.match(CalculatorParser.T__1)
            self.state = 24
            self.expr(0)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 25
                self.match(CalculatorParser.T__2)
                self.state = 26
                self.match(CalculatorParser.ID)
                self.state = 27
                self.match(CalculatorParser.T__1)
                self.state = 28
                self.expr(0)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.ExprContext,i)


        def ID(self):
            return self.getToken(CalculatorParser.ID, 0)

        def INT(self):
            return self.getToken(CalculatorParser.INT, 0)

        def condExpr(self):
            return self.getTypedRuleContext(CalculatorParser.CondExprContext,0)


        def getRuleIndex(self):
            return CalculatorParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalculatorParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 35
                self.match(CalculatorParser.T__7)
                self.state = 36
                self.expr(0)
                self.state = 37
                self.match(CalculatorParser.T__8)
                pass

            elif la_ == 2:
                self.state = 39
                self.match(CalculatorParser.ID)
                pass

            elif la_ == 3:
                self.state = 40
                self.match(CalculatorParser.INT)
                pass

            elif la_ == 4:
                self.state = 41
                self.condExpr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 50
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = CalculatorParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 45
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 46
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = CalculatorParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 48
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 49
                        self.expr(6)
                        pass

             
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CondExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.ExprContext,i)


        def relOp(self):
            return self.getTypedRuleContext(CalculatorParser.RelOpContext,0)


        def getRuleIndex(self):
            return CalculatorParser.RULE_condExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondExpr" ):
                listener.enterCondExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondExpr" ):
                listener.exitCondExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondExpr" ):
                return visitor.visitCondExpr(self)
            else:
                return visitor.visitChildren(self)




    def condExpr(self):

        localctx = CalculatorParser.CondExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(CalculatorParser.T__7)
            self.state = 56
            self.expr(0)
            self.state = 57
            self.relOp()
            self.state = 58
            self.expr(0)
            self.state = 59
            self.match(CalculatorParser.T__8)
            self.state = 60
            self.match(CalculatorParser.T__9)
            self.state = 61
            self.expr(0)
            self.state = 62
            self.match(CalculatorParser.T__10)
            self.state = 63
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorParser.RULE_relOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelOp" ):
                listener.enterRelOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelOp" ):
                listener.exitRelOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelOp" ):
                return visitor.visitRelOp(self)
            else:
                return visitor.visitChildren(self)




    def relOp(self):

        localctx = CalculatorParser.RelOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_relOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




