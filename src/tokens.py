#Data types
Token_INTEGER      = 'NUMBER_INTEGER'
Token_FLOAT        = 'NUMBER_FLOAT'
Token_STRING       = 'TEXT_STRING'
Token_CHAR         = 'TEXT_CHAR'
Token_VAR          = 'VARIABLE'

#aritmetic_op
Token_PLUS         = 'PLUS'
Token_MINUS        = 'MINUS'
Token_MUL          = 'MUL'
Token_DIV          = 'DIV'

#Variables types
Token_Type_BOOLEAN = 'TypeBoolean'
Token_Type_STRING  = 'TypeString'
Token_Type_CHAR    = 'TypeChar'
Token_Type_INTEGER = 'TypeInteger'
Token_Type_FLOAT   = 'TypeFloat'

#Control_Structures
Token_CONDITIONAL  = 'CONDITIONAL'
Token_LOOP         = 'LOOP'
Token_BREAK        = 'BREAK'
Token_RETURN       = 'RETURN'

#Logical_op
Token_NOT = 'LOGICAL_OP_NOT'
Token_AND = 'LOGICAL_OP_AND'
Token_OR  = 'LOGICAL_OP_OR'

#Special_values
Token_TRUE  = 'TRUE'
Token_FALSE = 'FALSE'
Token_NULL  = 'NULL'

#Operators
Token_ASSIGNMENT_OP    = 'ASSIGNMENT_OP'
Token_EQUAL_OP         = 'EQUAL_OP'
Token_DIFF_OP          = 'DIFFERENT_OP'
Token_GREATER_OP       = 'GREATER_OP'
Token_LESS_OP          = 'LESS_OP'
Token_GREATER_EQUAL_OP = 'GREATER_EQUAL_OP'
Token_LESS_EQUAL_OP    = 'LESS_EQUAL_OP'

#Symbols
Token_LPAREN     = 'LPAREN'
Token_RPAREN     = 'RPAREN'
Token_SEPARATION = 'SEPARATION'
Token_START_STR  = 'START_STRING'
Token_START_COMM = 'START_COMMENT'
Token_END        = 'END_LINE'

#function
Token_FUNCT_DECLARATION = 'FUNCTION_DECLARATION'

class Token:
    def __init__(self, type, value = None):
        self.type = type
        self.value = value

    def __repr__(self) -> str:
        return f'{self.type}:'+"{"+f'{self.value}'+"}"