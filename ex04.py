num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
maior = 0
menor = 0
meio = 0
# Número 1 é o maior
if (num1 > num2 and num1 > num3):
    maior = num1
    if (num2 < num3):
        menor = num2
        meio = num3
    else:
        menor = num3
        meio = num2
# Número 2 é o maior
elif (num2 > num1 and num2 > num3):
    maior = num2
    if (num1 < num3):
        menor = num1
        meio = num3
    else:
        menor = num3
        meio = num1
# Número 3 é o maior
else:
    maior = num3
    if (num2 < num1):
        menor = num2
        meio = num1
    else:
        menor = num1
        meio = num2

# Todos números iguais
if (num1 == num2 and num1 == num3 and num2 == num3):
    print("Você digitou números iguais...")
else:
    print(menor, meio, maior)