#Basic JSON parser
TT_LBrace = 'LBrace'
TT_RBrace = 'RBrace'
TT_Comma = 'Comma'
TT_Colon = 'Colon'
TT_String = 'String'
TT_Unknown = 'Unknown'

characters =  ['a','b','c','d']

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    #Read up on this
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

#Consume the string and create a list of tokens
class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char == '{':
                tokens.append(Token(TT_LBrace))
                self.advance()
            elif self.current_char == '}':
                tokens.append(Token(TT_RBrace))
                self.advance()
            elif self.current_char == ',':
                tokens.append(Token(TT_Comma))
                self.advance()
            elif self.current_char == ':':
                tokens.append(Token(TT_Colon))
                self.advance()
            elif self.current_char == '"':
                self.advance()
                tok = self.make_character()
                tokens.append(tok)
                self.advance()
            else:
                raise Exception('Illegal Character!')
        return tokens

    def make_character(self):
        char_str = ''
        while(self.current_char != None):
            if(self.current_char == "\""):
                self.advance()
                return Token(TT_String, char_str)
            elif(self.current_char in characters):
                print(self.current_char)
                char_str+=self.current_char
                self.advance()
            else:
                raise Exception('Illegal Character!')

class Parser:
    def __init__(self,tokens):
        self.tokens=tokens
        self.pos=0
    def parse(self):
        if self.tokens[self.pos] is TT_LBrace:
            self.next_token()
        elif self.tokens[self.pos] is TT_String:
            self.next_token()
        elif self.tokens[self.pos] is TT_Colon:
            self.next_token()
        elif self.tokens[self.pos] is TT_String:
            self.next_token()
        elif self.tokens[self.pos] is TT_Comma:
            self.next_token()
        elif self.tokens[self.pos] is TT_String:
            self.next_token()
        elif self.tokens[self.pos] is TT_Colon:
            self.next_token()
        elif self.tokens[self.pos] is TT_String:
            self.next_token()
        elif self.tokens[self.pos] is TT_RBrace:
            self.next_token()
        else:
            raise Exception('Wrong format!')

    def next_token(self):
        self.pos+=1
        self.tokens[self.pos]

lexer = Lexer("", '{"bdc":"bac","abc":"bca"}')
tokens = lexer.make_tokens()
parser = Parser(tokens)

# Should throw an exception
lexer = Lexer("", '{"bdc":"bac","abcf":"bca"}')
tokens = lexer.make_tokens()
parser = Parser(tokens)
