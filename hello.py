import calendar
import time

print ("Hello python!")
#declaração dos valores
h=1
o=8

disciplinas=["Física","Química","Biologia","História","Geografia","Ciências"]

#impressão em console das variáveis
print("H é: ",h)
print("O é: ",o)

#operações aritméticas com as variáveis
soma=h+o
print("H + O é: ",soma)

multi=h*o
print("H vezes O é: ",multi)


print("\n")
print(disciplinas)
print("\n")

disciplinas=["Física","Química","Biologia","História","Geografia","Ciências"]

with open("disciplinas.txt","w") as materiasW:
    for listitem in disciplinas:
        materiasW.write("%s\n"%listitem)