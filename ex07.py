num = int(input("Digite um número inteiro: "))
if (num % 5 == 0 and num % 10 == 0):
    print(f'{num} é divisivel por 5 e 10 ao mesmo tempo')
else:
    print(f'{num} não é divisivel por 5 e 10 ao mesmo tempo')