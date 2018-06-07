from lexer import Lexer

def main():
    filename = "testEASY.skip"
    file = open(filename,'r')
    lexer = Lexer(file)

    lexer.tokenizer()
    print("TOKENS:")
    print(lexer.tokens, "\n")

if __name__ == "__main__":
    main()
