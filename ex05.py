num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if (num1 < num2 and num1 < num3):
    if (num3 > num2):
        print("Os números foram digitados em ordem crescente.")
    else:
        print("Os números não foram digitados em ordem crescente.")
else:
    print("Os números não foram digitados em ordem crescente.")