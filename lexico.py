from ply import lex
from ply import yacc

keywords = {
	'def': 'DEF',
	'break': 'BREAK',
	'read': 'READ',
	'return': 'RETURN',
	'if': 'IF',
	'else': 'ELSE',
	'for': 'FOR',
	'new': 'NEW',
	'null': 'NULL',
	'print': 'PRINT',
	'int': 'INT',
	'float': 'FLOAT',
	'string': 'STRING',
}

tokens = list(keywords.values()) + [
	'IDENT', 'INT_CONSTANT',
	'FLOAT_CONSTANT', 'STRING_CONSTANT',
	'LPARENTESES', 'RPARENTESES', 'LBRACKET', 'RBRACKET',
	'LCURLYBRACKET', 'RCURLYBRACKET', 'SEMICOLON', 'COMMA',
	'ASSIGNMENT', 'EQUAL', 'MINUS', 'PLUS', 'LESSTHAN', 
	'GREATERTHAN', 'LESSEQUAL', 'GREATEREQUAL', 'DIFFERENT',
	'DIV', 'MOD', 'MULT'
]

def t_IDENT(t):
	r'[a-zA-Z][a-zA-Z0-9_]*'
	t.type = keywords.get(t.value, 'IDENT')
	return t


def t_FLOAT_CONSTANT(t):
	r'\d+\.\d+(E[+-]?\d+)?'
	return t
	
def t_INT_CONSTANT(t):
	r'\d+'
	return t


def t_STRING_CONSTANT(t):
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

t_ignore = ' \t'

def t_COMMENT(t):
	r'\#.*'	
	pass

# t_ignore_COMMENT = r'\#.*'

# Define a rule so we can track line numbers
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
	t.lexer.colno = 1

# Compute column.
#     input is the input text string
#     token is a token instance
def find_column(input, token):
	line_start = input.rfind('\n', 0, token.lexpos) + 1
	return (token.lexpos - line_start) + 1

# TODO:
# Error handling rule
def t_error(t):
	print(t.lexer.lexpos)
	# print(f"Illegal character {t.value[0]} at line {t.lexer.lineno} character {find_column(t.lexer.line, t.value[0])}")
	print(f"Illegal character {t.value[0]} at line {t.lexer.lineno} column {t.lexer.colno}")
	t.lexer.skip(1)


with open("exemplo1.lcc", 'r+') as f:
	data = f.read()

lexer = lex.lex()
lexer.input(data)

# # with open('out.txt', 'w') as f:
while True:
	tok = lexer.token()
	if not tok: 
		break     # No more input
	print(tok)
# 		# f.write(str(tok))