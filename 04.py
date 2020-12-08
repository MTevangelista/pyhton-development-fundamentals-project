"""
Escreva um programa em Python que leia um vetor de 5 números inteiros e o apresente na ordem inversa. Imprima o vetor no final. Use listas.
Exemplo: se a entrada for [4, 3, 5, 1, 2], o resultado deve ser [2, 1, 5, 3, 4].
"""

numbers = []

for i in range(1, 5+1):
    number = int(input(f"Entre com o {i} número:\n"))

    while number < 0:
        print('Erro, o número precisar inteiro!')
        number = int(input(f"Entre com o {i} número:\n"))
    
    numbers.append(number)

print(f"ordem normal: {numbers}")
numbers.reverse()
print(f"ordem inversa: {numbers}")