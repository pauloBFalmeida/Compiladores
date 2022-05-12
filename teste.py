from ply import lex
from ply import yacc

keywords = (
	'DEF', 'BREAK', 'READ', 'RETURN', 'IF', 'ELSE',
	'FOR', 'NEW', 'NULL', 'PRINT'	
)

tokens = keywords + (
	'IDENT', 'INT', 'FLOAT', 'STRING', 'INT_CONSTANT',
	'FLOAT_CONSTANT', 'STRING_CONSTANT',
	'LPARENTESES', 'RPARENTESES', 'LBRACKET', 'RBRACKET',
	'LCURLYBRACKET', 'RCURLYBRACKET', 'SEMICOLON', 'COMMA',
	'ASSIGNMENT', 'EQUAL', 'MINUS', 'PLUS', 'LESSTHAN', 
	'GREATERTHAN', 'LESSEQUAL', 'GREATEREQUAL', 'DIFFERENT',
	'DIV', 'MOD', 'MULT'
)

def t_IDENT(t):
	r'[a-zA-Z][a-zA-Z0-9_]*'
	if t.value in keywords:
		t.type = t.value
	return t


def t_INT(t):
	r'[0-9]+'
	return t

def t_FLOAT(t):
	r'\d+\.\d+(E[+-]?\d+)?'
	return t

def t_STRING(t):
	r'\".*?\"'
	return t

t_LPARENTESES = r'\('
t_RPARENTESES = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCURLYBRACKET = r'{'
t_RCURLYBRACKET = r'}'
t_SEMICOLON = r';'
t_COMMA = r'\,'
t_ASSIGNMENT = r'='
t_EQUAL 	= r'=='
t_MINUS 	= r'-'
t_PLUS 		= r'\+' 
t_LESSTHAN	= r'<'
t_GREATERTHAN	= r'>'
t_LESSEQUAL		= r'<='
t_GREATEREQUAL	= r'>='
t_DIFFERENT		= r'!='
t_DIV	= r'/'
t_MOD	= r'%'
t_MULT	= r'\*'


def t_COMMENT(t):
     r'\#.*'
     pass

t_ignore_COMMENT = r'\#.*'

# Define a rule so we can track line numbers
 def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

# Compute column.
 #     input is the input text string
 #     token is a token instance
 def find_column(input, token):
     line_start = input.rfind('\n', 0, token.lexpos) + 1
     return (token.lexpos - line_start) + 1

# TODO:
# # Error handling rule
# def t_error(t):
#      print("Illegal character '%s' at line '%i' character '%i'" 
#      		% t.value[0], %t.lexer.lineno, find_column())
#      t.lexer.skip(1)
