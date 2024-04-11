
Token_INTEGER      = 'NUMBER'
Token_FLOAT        = 'FLOAT'
Token_VAR          = 'VARIABLE'

Token_Type_BOOLEAN = 'TypeBoolean'
Token_Type_STRING  = 'TypeString'
Token_Type_CHAR    = 'TypeChar'
Token_Type_INTEGER = 'TypeInteger'
Token_Type_FLOAT   = 'TypeFloat'

Token_PLUS         = 'PLUS'
Token_MINUS        = 'MINUS'
Token_MUL          = 'MUL'
Token_DIV          = 'DIV'

Token_LPAREN       = 'LPAREN'
Token_RPAREN       = 'RPAREN'
Token_END          = 'ENDLINE'

Token_CONDITIONAL  = 'CONDITIONAL_OP'
Token_LOGICAL_OP   = 'LOGICAL_OP'
Token_ASSIGNMENT_OP = 'ASSIGNMENT_OP'

class Token:
    def __init__(self, type, value = None):
        self.type = type
        self.value = value

    def __repr__(self) -> str:
        return f'{self.type}:'+"{"+f'{self.value}'+"}"