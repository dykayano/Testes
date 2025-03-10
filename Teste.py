user_input = int(input("Digite um número inteiro: "))
print(user_input)
if user_input>0:
    cond1="É positivo."
elif user_input<0:
    cond1="É negativo."
else: cond1="É nulo."
print(cond1)
if user_input % 2 == 0:
    cond2="É par."
else: cond2 = "É ímpar."
print(cond2)
if user_input % 3 == 0:
    cond3 = "É divisível por 3."
else: cond3 = "Não é divisível por 3."
print(cond3)