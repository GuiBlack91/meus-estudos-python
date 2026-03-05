notas_de_alunos = [9, 5, 7, 8, 6, 10, 4, 3, 2, 1]
soma = sum(notas_de_alunos)
quantidade = len(notas_de_alunos)
print(soma)
print(quantidade)

media = soma / quantidade

print ("A soma das notas é:", soma)
print ("A quantidade de notas é:", quantidade)
print ("A média das notas é:", media)

if media >= 5:
 print("Parabéns, você foi aprovado")

else: media < 5
print("Infelizmente, você foi reprovado.")
