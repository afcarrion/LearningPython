# -*- coding: utf-8 -*-
"""DecimalARomano.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uhTJxDXeZSnr2jSF9j72An1KerUuK_yS
"""

numeroDecimal = input("Digite un numero del 1 al 3999: ")
numeroDecimal = int(numeroDecimal) 
print(
    "V = 5",
    "X = 10",
    "L = 50",
    "C = 100",
    "D = 500",
    "M = 1000"
)
miles = numeroDecimal / 1000
centena = (numeroDecimal / 100) % 10
decena = (numeroDecimal / 10) % 10
unidad = numeroDecimal % 10

print(miles, centena, decena, unidad)
milesInt = int(miles)
centenaInt = int(centena)
decenaInt = int(decena)
unidadInt = int(unidad)
print(milesInt)
print(centenaInt)
print(unidadInt)
numeroRomano = ""


#Miles
i = 1
while i <= milesInt:
  numeroRomano = numeroRomano + "M"
  i = i+1

#Centenas
if (centenaInt == 9):
  numeroRomano = numeroRomano + "CM"
elif centenaInt >= 5:
  numeroRomano = numeroRomano + "D"
  j = 6
  while j <= centenaInt:
    numeroRomano = numeroRomano + "C"
    j = j + 1
elif centenaInt == 4:
    numeroRomano = numeroRomano + "CD"
else:
  k = 1
  while k <= centenaInt:
    numeroRomano = numeroRomano + "C"
    k = k + 1

#Decenas
if(decenaInt == 9):
  numeroRomano = numeroRomano + "XC"
elif decenaInt >= 5:
  numeroRomano = numeroRomano + "L"
  i = 6
  while i <= decenaInt:
    numeroRomano = numeroRomano + "X"
    i = i + 1
elif decenaInt == 4:
  numeroRomano = numeroRomano + "XL"
else:
  i=1
  while i <= decenaInt:
    numeroRomano = numeroRomano + "X"
    i = i + 1

#Unidades

if(unidadInt == 9):
  numeroRomano = numeroRomano + "IX"
elif unidadInt >= 5:
  numeroRomano = numeroRomano + "V"
  i = 6
  while i <= unidadInt:
    numeroRomano = numeroRomano + "I"
    i = i + 1
elif unidadInt == 4:
  numeroRomano = numeroRomano + "IV"
else:
  i=1
  while i <= unidadInt:
    numeroRomano = numeroRomano + "I"
    i = i + 1


print(numeroRomano)