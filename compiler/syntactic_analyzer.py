import compiler.ply.yacc as yacc
from compiler.lexical_analyzer import CC20221Lexer
from compiler.ply.lex import LexToken


class CC20221SyntaxError(Exception):
    pass


class CC20221SyntacticAnalyzer:
    """Syntatic Analyser for CC20221 grammar"""

    def __init__(self, **kwargs):
        self.lexer = CC20221Lexer()
        self.tokens = self.lexer.tokens
        self.parser = yacc.yacc(start="PROGRAM", module=self, **kwargs)

    def p_error(self, p):
        sentence = [i.type if isinstance(i, LexToken) else str(i) for i in self.parser.symstack]
        raise CC20221SyntaxError(f"Syntax error in symbol {self.parser.symstack[-1]} on token {p} in stack: {' '.join(sentence[1:])}")

    def p_empty(self, p):
        "empty :"
        pass

    def p_prog_statement(self, p):
        """PROGRAM  : STATEMENT
                    | FUNCLIST
                    | empty"""
        pass

    def p_funclist(self, p):
        "FUNCLIST : FUNCDEF FUNCLISTAUX"
        pass

    def p_funclistaux(self, p):
        """FUNCLISTAUX  : FUNCLIST
                        | empty"""
        pass

    def p_fundef(self, p):
        "FUNCDEF : DEF IDENT LPARENTHESIS PARAMLIST RPARENTHESIS LCURLYBRACKET STATELIST RCURLYBRACKET"
        pass

    def p_paramlist(self, p):
        """PARAMLIST    : DATATYPE IDENT PARAMLISTAUX
                        | empty"""
        pass

    def p_paramlist_aux(self, p):
        """PARAMLISTAUX : COMMA PARAMLIST
                        | empty"""
        pass

    def p_datatype(self, p):
        """DATATYPE : INT
                    | FLOAT
                    | STRING"""
        pass

    def p_statement_vardecl(self, p):
        "STATEMENT : VARDECL SEMICOLON"
        pass

    def p_statement_atrib(self, p):
        "STATEMENT : ATRIBSTAT SEMICOLON"
        pass

    def p_statement_print(self, p):
        "STATEMENT : PRINTSTAT SEMICOLON"
        pass

    def p_statement_read(self, p):
        "STATEMENT : READSTAT SEMICOLON"
        pass

    def p_statement_return(self, p):
        "STATEMENT : RETURNSTAT SEMICOLON"
        pass

    def p_statement_if(self, p):
        "STATEMENT : IFSTAT"
        pass

    def p_statement_for(self, p):
        "STATEMENT : FORSTAT"
        pass

    def p_statement_state(self, p):
        "STATEMENT : LCURLYBRACKET STATELIST RCURLYBRACKET"
        pass

    def p_statement_term(self, p):
        """STATEMENT    : BREAK SEMICOLON
                        | SEMICOLON"""
        pass

    def p_vardecl(self, p):
        "VARDECL : DATATYPE IDENT OPTIONAL_VEC"
        pass

    def p_optional_vec(self, p):
        """OPTIONAL_VEC : LBRACKET INT_CONSTANT RBRACKET OPTIONAL_VEC
                        | empty"""
        pass

    def p_atribstat(self, p):
        "ATRIBSTAT : LVALUE ASSIGNMENT R_ATRIB"
        pass

    def p_r_atrib(self, p):
        """R_ATRIB  : EXPRESSION
                    | ALLOCEXPRESSION
                    | FUNCCALL"""
        pass

    def p_funccall(self, p):
        "FUNCCALL : IDENT LPARENTHESIS PARAMLISTCALL RPARENTHESIS"
        pass

    def p_paramlistcall(self, p):
        "PARAMLISTCALL : IDENT PARAMLISTCALLAUX"
        pass

    def p_paramlistcall_aux(self, p):
        """PARAMLISTCALLAUX : COMMA PARAMLISTCALL
                            | empty"""
        pass

    def p_printstat(self, p):
        "PRINTSTAT : PRINT EXPRESSION"
        pass

    def p_readstat(self, p):
        "READSTAT : READ LVALUE"
        pass

    def p_returnstat(self, p):
        "RETURNSTAT : RETURN"
        pass

    def p_ifstat(self, p):
        "IFSTAT : IF LPARENTHESIS EXPRESSION RPARENTHESIS STATEMENT IFAUX"
        pass

    def p_ifaux(self, p):
        """IFAUX    : ELSE STATEMENT
                    | empty"""
        pass

    def p_forstat(self, p):
        "FORSTAT : FOR LPARENTHESIS ATRIBSTAT SEMICOLON EXPRESSION SEMICOLON ATRIBSTAT RPARENTHESIS STATEMENT"
        pass

    def p_statelist(self, p):
        "STATELIST : STATEMENT OPT_STATELIST"
        pass

    def p_opt_statelist(self, p):
        """OPT_STATELIST    : STATELIST
                            | empty"""
        pass

    def p_allocexp(self, p):
        "ALLOCEXPRESSION : NEW DATATYPE LBRACKET NUMEXPRESSION RBRACKET OPT_NUMEXPRESSION"
        pass

    def p_opt_numexpression(self, p):
        """OPT_NUMEXPRESSION    : LBRACKET NUMEXPRESSION RBRACKET OPT_NUMEXPRESSION
                                | empty"""
        pass

    def p_expression(self, p):
        "EXPRESSION : NUMEXPRESSION OPT_REL_OP_NUM_EXPRESSION"
        pass

    def p_opt_rel_op_num_expression(self, p):
        """OPT_REL_OP_NUM_EXPRESSION    : REL_OP NUMEXPRESSION
                                        | empty"""
        pass

    def p_relop_lt(self, p):
        """REL_OP   : LESSTHAN
                    | GREATERTHAN
                    | LESSEQUAL
                    | GREATEREQUAL
                    | EQUAL
                    | DIFFERENT"""
        pass

    def p_numexpression(self, p):
        "NUMEXPRESSION : TERM OTHERTERM"
        pass

    def p_otherterm(self, p):
        """OTHERTERM    : PLUS_OR_MINUS TERM OTHERTERM
                        | empty"""
        pass

    def p_plus_or_minus(self, p):
        """PLUS_OR_MINUS    : PLUS
                            | MINUS"""
        pass

    def p_term(self, p):
        "TERM : UNARYEXPR OPT_UNARYEXPR"
        pass

    def p_opt_unary_expr(self, p):
        """OPT_UNARYEXPR    : OPERATOR UNARYEXPR OPT_UNARYEXPR
                            | empty"""
        pass

    def p_operator(self, p):
        """OPERATOR : MULT
                    | MOD
                    | DIV"""
        pass

    def p_unary_exp(self, p):
        """UNARYEXPR    : PLUS_OR_MINUS FACTOR
                        | FACTOR"""
        pass

    def p_factor_const(self, p):
        """FACTOR : INT_CONSTANT
                    | FLOAT_CONSTANT
                    | STRING_CONSTANT
                    | NULL
                    | LVALUE"""
        pass

    def p_factor_numexpression(self, p):
        "FACTOR : LPARENTHESIS NUMEXPRESSION RPARENTHESIS"
        pass

    def p_lvalue(self, p):
        "LVALUE : IDENT OPT_NUMEXPRESSION"
        pass

    def parse(self, source_code: str, **kwargs):
        self.parser.parse(source_code, lexer=self.lexer, **kwargs)
