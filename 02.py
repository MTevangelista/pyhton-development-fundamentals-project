"""
Escreva um programa em Python que some todos os números pares de 1 até um dado n, inclusive. O dado n deve ser obtido do usuário. No final, escreva o valor do resultado desta soma.
"""

number = 3
sum_of_values = 0

for index in range(1, 10+1): 
    if index % 2 == 0:
        sum_of_values += index

print(sum_of_values)
