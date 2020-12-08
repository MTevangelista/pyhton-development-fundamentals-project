"""
Escreva um programa em Python que leia uma tupla contendo n números inteiros, (n1, n2, n3 .. n) e os imprima em ordem crescente.
"""

numbers = []
number = int(input("Entre com número inteiro:\n"))

while number > 0:
    numbers.append(number)    
    number = int(input("Entre com número inteiro:\n"))

numbers = tuple(numbers)
print(numbers)

list_of_ordered_numbers = tuple(sorted(numbers))
print(list_of_ordered_numbers)