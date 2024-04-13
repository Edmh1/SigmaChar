import re
import tokens as t
import error


#                 boolean     string     char     int     float     
type_variables = ['STATUS', 'GIGACHAD', 'CHAD', 'SIGMA', 'REAL']
#                       if       else    while         for        break      return
control_structures = ['ALPHA', 'BETA','ALPHA_LOOP','BETA_LOOP', 'BYEBYE', 'ELEVATE']
#                      NOT      AND     OR    
logicals_operators = ['FAKE', 'MOGGED', 'GOD']
#                 TRUE      FALSE     NULL
special_values = ['VERUM', 'FALSUM', 'NIHIL']
#             =    EQUAL  DIFF  >  <   >=   <=     
operators = ['->', '==', '!=','>','<' '>=', '<=']
#            (    )    ,    "    #    ;
symbols = ['(', ')', ',', '@', '//', '$']
#                       def
function_key_word = 'COMMAND'


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None
    
    def peek(self):
        peek_pos = self.pos + 1
        if peek_pos < len(self.text):
            return self.text[peek_pos]
        else:
            return None

    def make_tokens(self):
        tokens = []

        while self.current_char is not None:
            if re.match(r'[ \t]', self.current_char):
                self.advance()
            #Data types
            elif re.match(r'[\d]', self.current_char):
                tokens.append(self.make_number())
            elif self.current_char == '@':
                self.advance()
                tokens.append(self.make_text())
            elif self.current_char == '$':
                tokens.append(t.Token(t.Token_END, "$"))
            
            elif self.current_char == '-' and self.peek() == '>':
                self.advance() 
                self.advance()
                tokens.append(t.Token(t.Token_ASSIGNMENT_OP, assignment_op))
            
            elif self.current_char == '+':
                tokens.append(t.Token(t.Token_PLUS, "+"))
                self.advance()
            elif self.current_char == '-':
                tokens.append(t.Token(t.Token_MINUS, "-"))
                self.advance()
            elif self.current_char == '*':
                tokens.append(t.Token(t.Token_MUL, "*"))
                self.advance()
            elif self.current_char == '/':
                tokens.append(t.Token(t.Token_DIV, "/"))
                self.advance()
            
            elif self.current_char == '(':
                tokens.append(t.Token(t.Token_LPAREN, "("))
                self.advance()
            elif self.current_char == ')':
                tokens.append(t.Token(t.Token_RPAREN, ")"))
                self.advance()
            else:
                char = self.current_char
                self.advance()
                return [], error.IllegalCharError("'"+char+"'")
        return tokens, None
    
    def make_number(self):
        num_str = ''
        has_dot = False

        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                if has_dot:
                    break
                has_dot = True
            num_str += self.current_char
            self.advance()
            
        if '.' in num_str:
            return t.Token(t.Token_FLOAT, float(num_str))
        else:
            return t.Token(t.Token_INTEGER, int(num_str))
    
    def make_text(self):
        txt_str = ''

        while self.current_char is not None:
            pass


        
def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens() 

    return tokens, error


