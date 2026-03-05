
nota1 = float(input ("Digite a primeira nota: "))
nota2 = float(input ("Digite a segunda nota: "))
nota3 = float(input ("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print ("A média das notas é:", media)

if media >= 6:
 print ("Parabéns, você foi aprovado.")

 elif media >= 4:
 print ("Você está de recuperação.")

else:
 print ("Infelizmente, você foi reprovado.")



