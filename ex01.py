trabalho_lab = float(input("Digite sua nota do laboratório: "))
avl_semestral = float(input("Digite sua nota da avaliação semestral: "))
exame_final = float(input("Digite sua nota do exame final: "))

# Peso das notas cálculo
# laboratório - peso 2 == 20%
# avaliação semestral - peso 3 == 30%
# exame final - peso 5 == 50%

peso_trabalho_lab = trabalho_lab * 0.2
peso_avl_semestral = avl_semestral * 0.3
peso_exame_final = exame_final * 0.5

media_ponderada = peso_trabalho_lab + peso_avl_semestral + peso_exame_final
print(media_ponderada)

if (media_ponderada >= 0 and media_ponderada < 5):
    print("Nota conceito E")
elif (media_ponderada >= 5 and media_ponderada < 6):
    print("Nota conceito D")
elif (media_ponderada >= 6 and media_ponderada < 7):
    print("Nota conceito C")
elif (media_ponderada >= 7 and media_ponderada < 8):
    print("Nota conceito B")
else:
    print("Nota conceito A")