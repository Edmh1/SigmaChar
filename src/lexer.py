import re
import tokens as t
import error

#
aritmetics_op = ['+','-','*','/']
#                 boolean     string     char     int     float     
variable_types = ['STATUS', 'GIGACHAD', 'CHAD', 'SIGMA', 'REAL']
#                       if       else    while         for        break      return
control_structures = ['ALPHA', 'BETA','ALPHA_LOOP','BETA_LOOP', 'BYEBYE', 'ELEVATE']
#                      NOT      AND     OR    
logical_operators = ['FAKE', 'MOGGED', 'GOD']
#                 TRUE      FALSE     NULL
special_values = ['VERUM', 'FALSUM', 'NIHIL']
#                       def
function_key_word = 'COMMAND'
#              =    <   >    <=   >=     EQUAL  DIFF  
operators = ['<-', '<', '>', '<=', '>=', '==', '!=']
#            (    )    ,    "    #    ;
symbols = ['(', ')', ',', '@', '#', '$']



class Lexer:
    def __init__(self, text):
        self.details = ''
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

    def missingChar(self, details):
        self.current_char = "¬"
        self.details = details


    def make_tokens(self):
        tokens = []

        while self.current_char is not None:
            if re.match(r'[ \t]', self.current_char):
                self.advance()
            #data types
            elif re.match(r'[\d]', self.current_char):
                tokens.append(self.make_number())
            elif self.current_char == '@':
                tokens.append(self.make_text())
            elif re.match(r'^[a-z]', self.current_char):
                tokens.append(t.Token(t.Token_VAR, self.make_var()))
            #aritmetic_op
            elif re.match(r'[+\-*\/]', self.current_char):
                if self.current_char == '+':
                    tokens.append(t.Token(t.Token_PLUS, "+"))
                elif self.current_char == '-':
                    tokens.append(t.Token(t.Token_MINUS, "-"))
                elif self.current_char == '*':
                    tokens.append(t.Token(t.Token_MUL, "*"))
                elif self.current_char == '/':
                    tokens.append(t.Token(t.Token_DIV, "/"))
                self.advance()
            #reserved words
            elif re.match(r'^[A-Z]', self.current_char):
                word = self.make_word()
                #variable types
                if word == "STATUS":
                    tokens.append(t.Token(t.Token_Type_BOOLEAN, word))
                elif word == "GIGACHAD":
                    tokens.append(t.Token(t.Token_Type_STRING, word))
                elif word == "CHAD":
                    tokens.append(t.Token(t.Token_Type_CHAR, word))
                elif word == "SIGMA":
                    tokens.append(t.Token(t.Token_Type_INTEGER, word))
                elif word == "REAL":
                    tokens.append(t.Token(t.Token_Type_FLOAT, word))
                #control structures
                elif word == "ALPHA":
                    tokens.append(t.Token(t.Token_CONDITIONAL, word))
                elif word == "BETA":
                    tokens.append(t.Token(t.Token_CONDITIONAL, word))
                elif word == "ALPHA_LOOP":
                    tokens.append(t.Token(t.Token_LOOP, word))
                elif word == "BETA_LOOP":
                    tokens.append(t.Token(t.Token_LOOP, word))
                elif word == "BYEBYE":
                    tokens.append(t.Token(t.Token_BREAK, word))
                elif word == "ELEVATE":
                    tokens.append(t.Token(t.Token_RETURN, word))
                #logical operators
                elif word == "FAKE":
                    tokens.append(t.Token(t.Token_NOT, word))
                elif word == "MOGGED":
                    tokens.append(t.Token(t.Token_AND, word))
                elif word == "GOD":
                    tokens.append(t.Token(t.Token_OR, word))
                #special values
                elif word == "VERUM":
                    tokens.append(t.Token(t.Token_TRUE, word))
                elif word == "FALSUM":
                    tokens.append(t.Token(t.Token_FALSE, word))
                elif word == "NIHIL":
                    tokens.append(t.Token(t.Token_NULL, word))
                #function
                elif word == "COMMAND":
                    tokens.append(t.Token(t.Token_FUNCT_DECLARATION))
                else:
                    char = word[0]
                    return [], error.IllegalCharError("'"+char+"'")
                self.advance()
            #operators
            elif self.current_char == '<':
                if self.peek() == '-':
                    self.advance()
                    self.advance()
                    tokens.append(t.Token(t.Token_ASSIGNMENT_OP, "<-"))
                elif self.peek() == '=':
                    self.advance()
                    self.advance()
                    tokens.append(t.Token(t.Token_LESS_EQUAL_OP, "<="))
                else:
                    tokens.append(t.Token(t.Token_LESS_OP, "<"))
                    self.advance()
            elif self.current_char == '>':
                if self.peek() == '=':
                    self.advance()
                    self.advance()
                    tokens.append(t.Token(t.Token_GREATER_EQUAL_OP, ">="))
                else:
                    tokens.append(t.Token(t.Token_GREATER_OP, ">"))
                    self.advance()
            elif self.current_char == '=' and self.peek() == '=':
                self.advance()
                self.advance()
                tokens.append(t.Token(t.Token_EQUAL_OP, "=="))
            elif self.current_char == '!' and self.peek() == '=':
                self.advance()
                self.advance()
                tokens.append(t.Token(t.Token_DIFF_OP, "!="))    
            #symbols
            elif self.current_char == '(':
                tokens.append(t.Token(t.Token_LPAREN, "("))
                self.advance()
            elif self.current_char == ')':
                tokens.append(t.Token(t.Token_RPAREN, ")"))
                self.advance()
            elif self.current_char == ',':
                tokens.append(t.Token(t.Token_SEPARATION, ","))
                self.advance()
            elif self.current_char == '#':
                tokens.append(self.make_comm())
            elif self.current_char == '$':
                tokens.append(t.Token(t.Token_END, "$"))
                self.advance()
            #errors
            elif self.current_char == '¬':
                return [], error.MissingCharTextError(self.details)
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
        count = 0

        while self.current_char is not None:
            if self.current_char == '@':
                count+=1
                if count == 2:
                    self.advance()
                    break
            else:
                txt_str += self.current_char
            self.advance()

        txt_str = "@"+txt_str+"@"
        if count == 2:
            if(txt_str.__len__() > 1):
                return t.Token(t.Token_STRING, txt_str) 
            else:
                return t.Token(t.Token_CHAR, txt_str)
        else:
            self.missingChar("@")
            return ""
        
    def make_comm(self):
        comm_str = ''
        count = 0

        while self.current_char is not None:
            if self.current_char == '#':
                count+=1
                if count == 2:
                    self.advance()
                    break
            else:
                comm_str += self.current_char
            self.advance()

        comm_str = "#"+comm_str+"#"
        if count == 2:
            return t.Token(t.Token_COMM, comm_str)
        else:
            self.missingChar("#")
            return ""
        
    def make_var(self):
        var_str = ''
        while self.current_char is not None:
            if self.current_char == ' ':
                break
            if self.current_char in aritmetics_op or self.current_char in operators or self.current_char in symbols:
                break
            var_str += self.current_char
            self.advance()
        return var_str
    
    def make_word(self):
        word_str = ''
        while self.current_char is not None:
            if self.current_char == ' ':
                break
            word_str += self.current_char
            self.advance()
        return word_str
    

def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens() 

    return tokens, error


