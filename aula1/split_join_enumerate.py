nn = '#'
#######################################################
print(f'{nn:#^60}')
n = ' Split '
print(f'{n:#^60}')
#######################################################
'''
Split, Join, Enumerate em Python
* Split - dividir uma string #str
* Join - Juntar uma lista # str
* Enumerate - Enumera elementos da lista #iteráveis
'''

s = 'O Brasil é o país do futebol, o Brasil é penta.'
lista_1 = s.split(' ')
print(lista_1)
lista_2 = s.split(',')
print(lista_2)
for valor in lista_2:
    print(valor)
for valor in lista_1:
    print(f'A palavra "{valor}" apareceu {lista_1.count(valor)}X na frase')
p=''
c=0
for valor in lista_1:
    qtd = lista_1.count(valor)
    if qtd > c:
        c = qtd
        p = valor
print(f'A palavra que tem mais é "{p}"  que apareceu {c}X')

for valor in lista_2:
    print(valor.strip().capitalize())  # strip remove espaco embranco do fim e do inicio e o
    # capitalize deixa a primeira letra maiuscula.

#######################################################
print(f'{nn:#^60}')
n = ' Join '
print(f'{n:#^60}')
#######################################################

string = '_'.join(lista_1)
print(string)

#######################################################
print(f'{nn:#^60}')
n = ' Indice '
print(f'{n:#^60}')
#######################################################

for indice, valor in enumerate(lista_1):
    print(indice, valor, lista_1[indice])

#######################################################
print(f'{nn:#^60}')
n = ' Lista '
print(f'{n:#^60}')
#######################################################

lista = [
    [1,2],
    [3,4],
    [5,6],
]
for v in lista:
    print(v[0], v[1])

#######################################################
print(f'{nn:#^60}')
#######################################################

lista = [
    [0,'Davi'],
    [1,'karine'],
    [2,'sofia'],
]
for indice, nome in lista:
    print(indice, nome)

#######################################################
print(f'{nn:#^60}')
n = ' = + de baixo utiliza enumerate '
print(f'{n:#^60}')
#######################################################

lista = ['Davi','karine','sofia']
for indice, nome in enumerate(lista):
    print(indice, nome)

#######################################################
print(f'{nn:#^60}')
n = ' Imprimir lista '
print(f'{n:#^60}')
#######################################################

n1, n2, n3 = lista
print(n2)

#######################################################
print(f'{nn:#^60}')
#######################################################

lista = [
    # 0    1    2
    ['A', 'B', 'C'],  # 0
    ['D', 'E', 'F'],  # 1
    ['G', 'H', 'Y'],  # 2
]
print(lista[0][2])

n = enumerate(lista)
print(n)
n = enumerate(lista)
n = list(n)
print(n)
'''
[
     0         1
    (0, ['A', 'B', 'C']),
          0    1    2
    (1, ['D', 'E', 'F']), 
    (2, ['G', 'H', 'Y'])]
'''
print(n[1][0])
print(n[1][1])
print(n[1][1][1])

#######################################################
print(f'{nn:#^60}')
n = ' For v1 e v2 '
print(f'{n:#^60}')
#######################################################

'''
lista = [
    # 0    1    2
    ['A', 'B', 'C'],  # 0
    ['D', 'E', 'F'],  # 1
    ['G', 'H', 'Y'],  # 2
]
'''
for v1, v2 in enumerate(lista, 53):
    print(v1,v2)
#######################################################
print(f'{nn:#^60}')
n = ' n = list  enumerate '
print(f'{n:#^60}')
#######################################################
n = list(enumerate(lista, 53))
print(n)
#######################################################
print(f'{nn:#^60}')
n = ' n = list  enumerate 2 '
print(f'{n:#^60}')
#######################################################
print(n[0][1][2])
#######################################################
print(f'{nn:#^60}')
n = ' Enumerate lista '
print(f'{n:#^60}')
#######################################################
for v1 in enumerate(lista, 53):
    print(v1)

#######################################################
print(f'{nn:#^60}')

