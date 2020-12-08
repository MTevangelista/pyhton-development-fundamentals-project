"""
Escreva uma função em Python que leia uma tupla contendo números inteiros, retorne uma lista contendo somente os números ímpares e uma nova tupla contendo somente os elementos nas posições pares.
"""

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def read_tuple(tuple_of_numbers):
    tuple_of_odd_numbers = []
    tuple_of_numbers = list(tuple_of_numbers)

    for number in numbers:
        if number % 2 != 0:
            tuple_of_numbers.remove(number)
            tuple_of_odd_numbers.append(number)
    
    tuple_of_numbers = tuple(tuple_of_numbers)
    
    return tuple_of_odd_numbers, tuple_of_numbers

print(read_tuple(numbers))