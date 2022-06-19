from compiler.ply import lex


class CC20221Lexer:
    """Lexical Analyzer for CC-2022-1 Language"""

    def __init__(self, **kwargs) -> None:
        self.lexer = lex.lex(module=self, **kwargs)

    keywords = {
        "def": "DEF",
        "break": "BREAK",
        "read": "READ",
        "return": "RETURN",
        "if": "IF",
        "else": "ELSE",
        "for": "FOR",
        "new": "NEW",
        "null": "NULL",
        "print": "PRINT",
        "int": "INT",
        "float": "FLOAT",
        "string": "STRING",
    }

    tokens = [
        *keywords.values(),
        "IDENT",
        "INT_CONSTANT",
        "FLOAT_CONSTANT",
        "STRING_CONSTANT",
        "LPARENTHESIS",
        "RPARENTHESIS",
        "LBRACKET",
        "RBRACKET",
        "LCURLYBRACKET",
        "RCURLYBRACKET",
        "SEMICOLON",
        "COMMA",
        "ASSIGNMENT",
        "EQUAL",
        "MINUS",
        "PLUS",
        "LESSTHAN",
        "GREATERTHAN",
        "LESSEQUAL",
        "GREATEREQUAL",
        "DIFFERENT",
        "DIV",
        "MOD",
        "MULT",
    ]

    def t_IDENT(self, t):
        r"[a-zA-Z][a-zA-Z0-9_]*"
        t.type = self.keywords.get(t.value, "IDENT")
        return t

    def t_FLOAT_CONSTANT(self, t):
        r"\d+\.\d+(E[+-]?\d+)?"
        return t

    def t_INT_CONSTANT(self, t):
        r"\d+"
        return t

    def t_STRING_CONSTANT(self, t):
        r"\".*?\""
        return t

    t_LPARENTHESIS = r"\("
    t_RPARENTHESIS = r"\)"
    t_LBRACKET = r"\["
    t_RBRACKET = r"\]"
    t_LCURLYBRACKET = r"{"
    t_RCURLYBRACKET = r"}"
    t_SEMICOLON = r";"
    t_COMMA = r"\,"
    t_ASSIGNMENT = r"="
    t_EQUAL = r"=="
    t_MINUS = r"-"
    t_PLUS = r"\+"
    t_LESSTHAN = r"<"
    t_GREATERTHAN = r">"
    t_LESSEQUAL = r"<="
    t_GREATEREQUAL = r">="
    t_DIFFERENT = r"!="
    t_DIV = r"/"
    t_MOD = r"%"
    t_MULT = r"\*"

    t_ignore = " \t"

    def t_COMMENT(self, t):
        r"\/\/.*"
        pass

    #  Define a rule so we can track line numbers
    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)
        t.lexer.colno = 1

    #  Error handling rule
    def t_error(self, t):
        raise IllegalTokenError(
            f"Illegal character {t.value[0]} at line {t.lineno} column {t.lexer.colno}"
        )

    def token(self):
        """Wrapper for token function"""
        return self.lexer.token()

    def input(self, source_code):
        """Wrapper for input function"""
        self.lexer.input(source_code)

    def tokenize(self, source_code):
        """Create list of tokens from source code"""
        self.input(source_code)
        tokens = []
        while True:
            tok = self.token()
            if not tok:
                break  # EOF
            tokens.append(tok)
        return tokens


class IllegalTokenError(Exception):
    """Lexical Analyser failed to parse code due to illegal character in token"""
