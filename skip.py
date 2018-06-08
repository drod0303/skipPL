from lexer import Lexer

def main():
    filename = "testEASY.skip"
    file = open(filename,'r')
    lexer = Lexer(file)
    parser = Parser(lexer.tokens)

    lexer.tokenizer()
    print("TOKENS:")
    for token in lexer.tokens:
        print(token)

    parser.build_AST()
    print("AST:")
    print(parser.AST)

if __name__ == "__main__":
    main()
