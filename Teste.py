while True:
    print("Digite um número inteiro: ")
    user_input = input("")
    try:
        val = int(user_input)
    except ValueError:
        print("Não é um número inteiro!")
        print()
        continue
    else:
        user_input=int(user_input)
        if user_input>0:
            cond1="é positivo."
        elif user_input<0:
            cond1="é negativo."
        else: cond1="é nulo."
        print(user_input, cond1)
        if user_input % 2 == 0:
            cond2="é par."
        else: cond2 = "é ímpar."
        print(user_input, cond2)
        if user_input % 3 == 0:
            cond3 = "é divisível por 3."
        else: cond3 = "não é divisível por 3."
        print(user_input, cond3)
        print()
