import time
import os
os.system ("cls || clear")

def limpar_terminal():
    import os
    os.system ("cls || clear")

lista_numero = []
quantidade_de_numeros = 5
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numero = 0
menor_numero = 0
soma_pares = 0
soma_impares = 0
soma_geral = 0
for i in range (quantidade_de_numeros):
    numero = int(input(f"Digite o {i+1}° número: "))
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1
        soma_impares += numero

    if numero < 0:
        quantidade_negativos += 1
    elif numero > 0:
        quantidade_positivos += 1

    maior_numero = max(maior_numero, numero)

    menor_numero = min(menor_numero, numero)

    soma_geral += numero

    lista_numero.append(numero)

    limpar_terminal()

media_pares = soma_pares / quantidade_pares
media_impares = soma_impares / quantidade_impares
media_geral = soma_geral / 5

print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")
print(f"Média de todos os números: {media_geral:.2f}")
print(f"Números na ordem inversa:")
for cada_numero in reversed (lista_numero):
    print (cada_numero)
    time.sleep(2)


