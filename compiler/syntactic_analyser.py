print("Build parser")

import ply.yacc as yacc

from lexical_analyser import CC20221Lexer

# Necessário para criar o parser com yacc
lexer = CC20221Lexer()
tokens = lexer.tokens


class CC20221SyntaxError(Exception):
    pass


# # TODO: uma mensagem de insucesso indicando qual é a entrada
# #  na tabela de reconhecimento sintático que está vazia (qual é a forma sentencial α,
# #  qual é o símbolo não-terminal mais à esquerda de α e qual é o token da entrada)
def p_error(p):
    # while True:
    #     token = parser.token()
    #     if not token or token.type == 'SEMICOLON':
    #         break
    # parser.errok()
    # return token
    raise CC20221SyntaxError(f"Syntax error in input {str(p)}")


# Gambiarra pra reconhecer uma sequência IDENT ATRIBSTAT
# considerando única e exclusivamente o exemplo 3
# def p_error(p):
#     if p.type == 'ASSIGNMENT':
#         prev_token = parser.symstack.pop()
#         if prev_token.type == "IDENT":
#             prev_token.type = "ATRIBSTAT"
#             while True:
#                 token = parser.token()
#                 if not token or token.type == 'SEMICOLON':
#                     break
#             #semicolon = parser.symstack.pop()
#             parser.symstack.append(prev_token)
#             #parser.symstack.append(semicolon)
#     parser.errok()
#     return token


def p_empty(p):
    'empty :'
    pass


def p_prog_statement(p):
    '''PROGRAM  : STATEMENT
                | FUNCLIST
                | empty'''
    # p[0] = p[1]
    pass


def p_funclist(p):
    'FUNCLIST : FUNCDEF FUNCLISTAUX'
    # p[0] = (p[1], p[2])
    pass


def p_funclistaux(p):
    '''FUNCLISTAUX  : FUNCLIST
                    | empty'''
    # p[0] = p[1]
    pass


def p_fundef(p):
    'FUNCDEF : DEF IDENT LPARENTHESIS PARAMLIST RPARENTHESIS LCURLYBRACKET STATELIST RCURLYBRACKET'
    # p[0] = (p[2], p[4], p[7])
    pass



def p_paramlist(p):
    '''PARAMLIST    : DATATYPE IDENT PARAMLISTAUX
                    | empty'''
    # if len(p) == 4:
    #     p[0] = (p[1], p[2], p[3])
    # else:
    #     p[0] = None
    pass


def p_paramlist_aux(p):
    '''PARAMLISTAUX : COMMA PARAMLIST
                    | empty'''
    # if len(p) == 3:
    #     p[0] = p[2]
    # else:
    #     p[0] = None
    pass


def p_datatype(p):
    '''DATATYPE : INT
                | FLOAT
                | STRING'''
    # p[0] = p[1]
    pass


def p_statement_vardecl(p):
    'STATEMENT : VARDECL SEMICOLON'
    # p[0] = p[1]
    pass


def p_statement_atrib(p):
    'STATEMENT : ATRIBSTAT SEMICOLON'
    # p[0] = p[1]
    pass


def p_statement_print(p):
    'STATEMENT : PRINTSTAT SEMICOLON'
    # p[0] = p[1]
    pass


def p_statement_read(p):
    'STATEMENT : READSTAT SEMICOLON'
    # p[0] = p[1]
    pass


def p_statement_return(p):
    'STATEMENT : RETURNSTAT SEMICOLON'
    # p[0] = p[1]
    pass


def p_statement_if(p):
    'STATEMENT : IFSTAT'
    # p[0] = p[1]
    pass


def p_statement_for(p):
    'STATEMENT : FORSTAT'
    # p[0] = p[1]
    pass


def p_statement_state(p):
    'STATEMENT : LCURLYBRACKET STATELIST RCURLYBRACKET'
    # p[0] = p[2]
    pass


def p_statement_term(p):
    '''STATEMENT    : BREAK SEMICOLON
                    | SEMICOLON'''
    pass


def p_vardecl(p):
    'VARDECL : DATATYPE IDENT OPTIONAL_VEC'
    # p[0] = (p[1], p[2], p[3])
    pass

def p_optional_vec(p):
    '''OPTIONAL_VEC : LBRACKET INT_CONSTANT RBRACKET OPTIONAL_VEC
                    | empty'''
    # if len(p) == 5:
    #     p[0] = (p[2], p[4])
    # else:
    #     p[0] = None
    pass
def p_atribstat(p):
    'ATRIBSTAT : LVALUE ASSIGNMENT R_ATRIB'
    # p[0] = (p[1], p[3])
    pass
# def p_atribstat(p):
#     '''ATRIBSTAT    : IDENT LBRACKET NUMEXPRESSION RBRACKET OPT_NUMEXPRESSION ASSIGNMENT R_ATRIB
#                     | IDENT ASSIGNMENT R_ATRIB'''
#     p[0] = (p[1], p[3])

# def p_atribstat_error(p):
#     'ATRIBSTAT    : error ASSIGNMENT R_ATRIB'
#     print("Syntax error in variable assignment statement. Bad expression")


def p_r_atrib(p):
    '''R_ATRIB  : EXPRESSION
                | ALLOCEXPRESSION
                | FUNCCALL'''
    # p[0] = p[1]
    pass


def p_funccall(p):
    'FUNCCALL : IDENT LPARENTHESIS PARAMLISTCALL RPARENTHESIS'
    # p[0] = (p[1], p[3])
    pass

def p_paramlistcall(p):
    'PARAMLISTCALL : IDENT PARAMLISTCALLAUX'
    # p[0] = (p[1], p[2])
    pass

def p_paramlistcall_aux(p):
    '''PARAMLISTCALLAUX : COMMA PARAMLISTCALL
                        | empty'''
    # if len(p) == 3:
    #     p[0] = p[2]
    # else:
    #     p[0] = None
    pass

# def p_funccall(p):
#     'FUNCCALL : IDENT LPARENTHESIS IDENT PARAMLISTCALLAUX RPARENTHESIS'
#     p[0] = (p[1], p[3])


# def p_paramlistcall_aux(p):
#     '''PARAMLISTCALLAUX : COMMA IDENT PARAMLISTCALLAUX
#                         | empty'''
#     if len(p) == 4:
#         p[0] = (p[2], p[3])
#     else:
#         p[0] = None


def p_printstat(p):
    'PRINTSTAT : PRINT EXPRESSION'
    # p[0] = p[2]
    pass


def p_readstat(p):
    'READSTAT : READ LVALUE'
    # p[0] = p[2]
    pass


def p_returnstat(p):
    'RETURNSTAT : RETURN'
    # p[0] = p[1]
    pass


def p_ifstat(p):
    'IFSTAT : IF LPARENTHESIS EXPRESSION RPARENTHESIS STATEMENT IFAUX'
    # p[0] = (p[3], p[5], p[6])
    pass

def p_ifaux(p):
    '''IFAUX    : ELSE STATEMENT
                | empty'''
    # if len(p) == 3:
    #     p[0] = p[2]
    # else:
    #     p[0] = None
    pass


def p_forstat(p):
    'FORSTAT : FOR LPARENTHESIS ATRIBSTAT SEMICOLON EXPRESSION SEMICOLON ATRIBSTAT RPARENTHESIS STATEMENT'
    # p[0] = (p[3], p[5], p[7], p[9])
    pass


def p_statelist(p):
    'STATELIST : STATEMENT OPT_STATELIST'
    # p[0] = (p[1], p[2])
    pass


def p_opt_statelist(p):
    '''OPT_STATELIST    : STATELIST
                        | empty'''
    # p[0] = p[1]
    pass


def p_allocexp(p):
    'ALLOCEXPRESSION : NEW DATATYPE LBRACKET NUMEXPRESSION RBRACKET OPT_NUMEXPRESSION'
    # p[0] = (p[2], p[4], p[6])
    pass


def p_opt_numexpression(p):
    '''OPT_NUMEXPRESSION    : LBRACKET NUMEXPRESSION RBRACKET OPT_NUMEXPRESSION
                            | empty''' 
    # if len(p) == 5:
    #     p[0] = (p[2], p[4])
    # else:
    #     p[0] = None
    pass

def p_expression(p):
    'EXPRESSION : NUMEXPRESSION OPT_REL_OP_NUM_EXPRESSION'
    # p[0] = (p[1], p[2])
    pass


def p_opt_rel_op_num_expression(p):
    '''OPT_REL_OP_NUM_EXPRESSION    : REL_OP NUMEXPRESSION
                                    | empty'''
    # if len(p) == 3:
    #     p[0] = (p[1], p[2])
    # else:
    #     p[0] = None
    pass


def p_relop_lt(p):
    '''REL_OP   : LESSTHAN
                | GREATERTHAN
                | LESSEQUAL
                | GREATEREQUAL
                | EQUAL
                | DIFFERENT'''
    # p[0] = p[1]
    pass


def p_numexpression(p):
    'NUMEXPRESSION : TERM OTHERTERM'
    # p[0] = (p[1], p[2])
    pass


def p_otherterm(p):
    '''OTHERTERM    : PLUS_OR_MINUS TERM OTHERTERM
                    | empty'''
    # if len(p) == 4:
    #     p[0] = (p[1], p[2], p[3])
    # else:
    #     p[0] = None
    pass

def p_plus_or_minus(p):
    '''PLUS_OR_MINUS    : PLUS
                        | MINUS'''
    # p[0] = p[1]
    pass


def p_term(p):
    'TERM : UNARYEXPR OPT_UNARYEXPR'
    # p[0] = (p[1], p[2])
    pass


def p_opt_unary_expr(p):
    '''OPT_UNARYEXPR    : OPERATOR UNARYEXPR OPT_UNARYEXPR
                        | empty'''
    # if len(p) == 4:
    #     p[0] = (p[1], p[2], p[3])
    # else:
    #     p[0] = None
    pass

def p_operator(p):
    '''OPERATOR : MULT
                | MOD
                | DIV'''
    # p[0] = p[1]
    pass

def p_unary_exp(p):
    '''UNARYEXPR    : PLUS_OR_MINUS FACTOR
                    | FACTOR'''
    # if len(p) == 3:
    #     p[0] = (p[1], p[2])
    # else:
    #     p[0] = p[1]
    pass

def p_factor_const(p):
    '''FACTOR : INT_CONSTANT
                | FLOAT_CONSTANT
                | STRING_CONSTANT
                | NULL
                | LVALUE'''
    # p[0] = p[1]
    pass


def p_factor_numexpression(p):
    'FACTOR : LPARENTHESIS NUMEXPRESSION RPARENTHESIS'
    # p[0] = p[2]
    pass


def p_lvalue(p):
    'LVALUE : IDENT OPT_NUMEXPRESSION'
    pass
    # p[0] = (p[1], p[2])

# Constrói parser
parser = yacc.yacc(start="PROGRAM", debug=True)

from pathlib import Path

EXAMPLES_PATH = Path(__file__).parents[1]

with (EXAMPLES_PATH / "examples/strings.lcc").open("r") as f:
    s = f.read()

result = parser.parse(s, debug=True, lexer=lexer)
print(result)
