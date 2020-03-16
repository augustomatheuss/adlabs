

# Listas e loops em Python


import copy


# Explicando a difetenca entre variavel e vetor
# num = 3
# vetor    [1, 2, 3, 4, 5]
# índices   0  1  2  3  4
# índices 0 até tamanho -1 = 0 até 5-1 = 0 até 4
print('O vetor:')
vetor = [5, 7, 9, 2, 6]
vetor2 = copy.deepcopy(vetor)  # Testar sem o deepcopy
vetor2[1] = -8

print(vetor)
print(vetor2)
print(vetor)

# Loop 1
print('\nPrimeiro loop:')
for i in range(len(vetor)):
    print('\tO valor do vetor na posição %d é %d' % (i, vetor[i]))

# Loop 2
# Tamanho é 4
print('\nSegundo loop')
frutas = ['laranja', 'maca', 'uva', 'pera']
for f in frutas:
    if f == 'uva':
        print('\tFruta uva foi encontrada no vetor!')

# Condicional - Exemplo 1
x = True
x = not x
print('\nCondicional - Exemplo 1:')
if x:
    print('\nX é verdadeiro')
else:
    print('\nX é falso')

# Condicional - Exemplo 2
print('\nCondicional - Exemplo 2:')
tamanho = 5
if len(vetor) == tamanho:
    print('\nO tamanho é %d' % tamanho)
else:
    print('\nO tamanho não é %d' % tamanho)

# Loop 3
# vetor [5, 7, 9, 2, 6]
print('\nTerceiro loop')
# O laco busca qual o indice do vetor onde ha um numero 9
indice = 0
# O laco while e processado enquanto as duas condicoes seguintes forem verdadeiras
# condicao 1: o valor do vetor na posicao indice e diferente de 9
# condicao 2? o valor do indice e menor do que o tamanho do vetor
while (indice < len(vetor)) and (vetor[indice] != 9):
    print('\tIndice atualizado de %d para %d' % (indice, indice+1))
    indice = indice + 1


# Teste para saber se o 9 foi encontrado
# Condicional - Exemplo 3
print('\nCondicional - Exemplo 3:')
if indice == len(vetor):
    print('\tO valor 9 nao foi encontrado no vetor ')
else:
    print('\tO valor 9 foi achado na posicao %d do vetor' % indice)

# Loop 4
print('\nQuarto loop')
# O laco e executado ate que a variavel seja maior do que 100
dobro = 2
while dobro < 100:
    print('O valor da variavel dobro e %d' % dobro)
    dobro *= 2  # dobro = dobro * 2
# Por causa da identacao o python entende que este print esta fora do laco while
print('....')

# Exemplos com lista
lista = []
lista2 = []
print(lista)

for i in range(7):
    lista.append(i)
    lista2.append(i*3.14)
print(lista)
print(lista2)

popp = lista[4]
lista.pop(4)
print(lista)
print(popp)

lista.extend(lista2)
print(lista)
lista.sort()
print(lista)


# Terminando o programa com sucesso
exit(0)
