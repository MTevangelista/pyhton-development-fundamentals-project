"""
Escreva uma função em Python chamada potencia. Esta função deve obter como argumentos dois números inteiros, A e B, e calcular AB usando multiplicações sucessivas (não use a função de python math.pow) e retornar o resultado da operação. Depois, crie um programa em Python que obtenha dois números inteiros do usuário e indique o resultado de AB usando a função.
"""

def potencia(base, expoente):
    potencia = 1

    for count in range(expoente):
        potencia *= base
        count += 1

    return potencia
    
base = int(input("Informe a base:\n"))
expoente = int(input("Informe o expoente:\n"))

result = potencia(base, expoente)

print(f"{base} ^ {expoente} = {result}")