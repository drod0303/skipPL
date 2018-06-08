class Lexer:

    def __init__(self,data):
        self.data = data
        self.tokens = []
        self.keywords = {

        'print',
        'num',
        'skip'

        }


    def tokenizer(self):
        for line in self.data:
            temp = []
            tempID = ''

            for character in line:
                if character == '"' and tempID == '':
                    tempID = 'STRING'
                    temp = []
                elif character == '"' and tempID == 'STRING':
                    self.tokens.append({'id': tempID, 'value': ''.join(temp)})
                    tempID = ''
                    temp = []
                elif character ==':':
                    self.tokens.append({'id': 'LABEL', 'value': ''.join(temp)})
                elif ''.join(temp) in self.keywords:
                    self.tokens.append({'id': 'KEYWORD', 'value': ''.join(temp)})
                    temp = []
                elif character == ' ' and tempID != 'STRING':
                    continue
                else:
                    temp.append(character)
