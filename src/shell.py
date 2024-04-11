import lexer

while True:
    text = input("nombreDelLenguaje > ")
    result, err = lexer.run(text)

    if err: 
        print(err.as_string())
    else: 
        print(result) 
