class Lexer:

    def __init__(self,data):
        self.data = data
        self.tokens = []
        self.keywords = {

        'print'

        }


    def tokenizer(self):
        for words in self.data:
            self.tokens.append(words)
