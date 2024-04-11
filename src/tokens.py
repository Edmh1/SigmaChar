
Token_INT      = 'INT'
Token_FLOAT    = 'FLOAT'
Token_PLUS     = 'PLUS'
Token_MINUS    = 'MINUS'
Token_MUL      = 'MUL'
Token_DIV      = 'DIV'
Token_LPAREN   = 'LPAREN'
Token_RPAREN   = 'RPAREN'


class Token:
    def __init__(self, type, value = None):
        self.type = type
        self.value = value

    def __repr__(self) -> str:
        return f'{self.type}:'+"{"+f'{self.value}'+"}"