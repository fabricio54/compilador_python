grammar Calculator;

prog:   stat+ ;

stat:   letDecl
    |   expr
    ;

letDecl: 'let' ID '=' expr (',' ID '=' expr)* ;

expr:   expr ('*'|'/') expr
    |   expr ('+'|'-') expr
    |   '(' expr ')'
    |   ID
    |   INT
    |   condExpr
    ;

condExpr: '(' expr relOp expr ')' '?' expr ':' expr ;

relOp:  '>' | '<' | '==' | '>=' | '<=' | '!=' ;

ID  :   [a-zA-Z]+ ;
INT :   [0-9]+ ;

WS  :   [ \t\r\n]+ -> skip ;
