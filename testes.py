import tabela
import funçoes
from tabela import rotor1
from tabela import rotor2
from tabela import rotor3
from tabela import rotor4
from tabela import rotor5
from tabela import espelho
from tabela import rotores
from tabela import letras
from tabela import numeros
from tabela import Nrotores
from tabela import msg
from tabela import Rescolhido
from tabela import Nescolhido
from tabela import funrot
from funçoes import inversor
from funçoes import rot
from funçoes import rot1
from funçoes import rot2
from funçoes import rot3
from funçoes import rot4
from funçoes import rot5
from funçoes import invrot1
from funçoes import invrot2
from funçoes import invrot3
from funçoes import invrot4
from funçoes import invrot5
from funçoes import espelho
from funçoes import convert

n = 1
while (n<4):
    rotores.append(input("selecione um rotor: "))
    letras.append(input("selecione sua respectiva letra: "))
    n += 1

i = 0
n = 1
while (n<4):
    numeros.append(inversor(letras[i]))
    Nrotores.append(rot(rotores[i]))
    n += 1
    i += 1


# A ser realizado

L = 'a'




Rescolhido.append(Nrotores[2])
Nescolhido.append(numeros[2])

if Nrotores[2] == rotor1:
    L = rot1(L)
elif Nrotores[2] == rotor2:
    L = rot2(L)
elif Nrotores[2] == rotor3:
    L = rot3(L)
elif Nrotores[2] == rotor4:
    L = rot4(L)
elif Nrotores[2] == rotor5:
    L = rot5(L)

print (L)

Rescolhido[0] = Nrotores[1]
Nescolhido[0] = numeros[1]

if Nrotores[1] == rotor1:
    L = rot1(L)
elif Nrotores[1] == rotor2:
    L = rot2(L)
elif Nrotores[1] == rotor3:
    L = rot3(L)
elif Nrotores[1] == rotor4:
    L = rot4(L)
elif Nrotores[1] == rotor5:
    L = rot5(L)

print (L)

Rescolhido[0] = Nrotores[0]
Nescolhido[0] = numeros[0]

if Nrotores[0] == rotor1:
    L = rot1(L)
elif Nrotores[0] == rotor2:
    L = rot2(L)
elif Nrotores[0] == rotor3:
    L = rot3(L)
elif Nrotores[0] == rotor4:
    L = rot4(L)
elif Nrotores[0] == rotor5:
    L = rot5(L)

print (L)

L = espelho(L)

print (L)

x = (Nrotores[0][numeros[0]])
y = x.rfind(L)

if Nrotores[0] == rotor1:
    L = invrot1(y)
elif Nrotores[0] == rotor2:
    L = invrot2(y)
elif Nrotores[0] == rotor3:
    L = invrot3(y)
elif Nrotores[0] == rotor4:
    L = invrot4(y)
elif Nrotores[0] == rotor5:
    L = invrot5(y)

print (L)

x = (Nrotores[1][numeros[1]])
y = x.rfind(L)

if Nrotores[1] == rotor1:
    L = invrot1(y)
elif Nrotores[1] == rotor2:
    L = invrot2(y)
elif Nrotores[1] == rotor3:
    L = invrot3(y)
elif Nrotores[1] == rotor4:
    L = invrot4(y)
elif Nrotores[1] == rotor5:
    L = invrot5(y)

print (L)

x = (Nrotores[2][numeros[2]])
y = x.rfind(L)

if Nrotores[2] == rotor1:
    L = invrot1(y)
elif Nrotores[2] == rotor2:
    L = invrot2(y)
elif Nrotores[2] == rotor3:
    L = invrot3(y)
elif Nrotores[2] == rotor4:
    L = invrot4(y)
elif Nrotores[2] == rotor5:
    L = invrot5(y)

print (L)













    

