nn = '#'
import time

# time.sleep(20)

#######################################################
print(f'{nn:#^60}')
n = ' Lista '
print(f'{n:#^60}')
#######################################################
"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
#      0    1    2    3    4
#     -5   -4   -3   -2   -1
lt = ['A', 'B', 'C', 'D', 'EFGH']  # lista
st = 'ABCDEFGH'  # string
print(st[-1])
print(lt[-1])
print(lt[1:3])
print(lt[::2])
print(lt[::-1])
lt1 = [1, 2, 3]
lt2 = [4, 5, 6]
lt3 = lt1 + lt2
print(f'lt1 = {lt1}')
print(f'lt2 = {lt2}')
print(f'lt3 = {lt3}')
#######################################################
print(f'{nn:#^60}')
n = ' lista.extend '
print(f'{n:#^60}')
#######################################################
lt2.extend(lt3)
print(f'lt2 extend(lt3) {lt2}')
lt2.extend('A')
print(f'let2 extend("A") {lt2}')
#######################################################
print(f'{nn:#^60}')
n = ' Lista.append '
print(f'{n:#^60}')
#######################################################
lt2.append('B')
print(f'lat2 append("B") {lt2}')
#######################################################
print(f'{nn:#^60}')
n = ' Lista.insert '
print(f'{n:#^60}')
#######################################################
lt2.insert(1, 'Davi')
print(f'lt2 insert(1, "Davi") {lt2}')
#######################################################
print(f'{nn:#^60}')
n = ' Lista.pop '
print(f'{n:#^60}')
#######################################################
x = lt2.pop()
print(f'lt2.pop() = {x}')
#######################################################
print(f'{nn:#^60}')
n = ' deletar da Lista '
print(f'{n:#^60}')
#######################################################
print(lt2)
del(lt2[2:4])
print(f'del(lt2[2:4]) lt2 fica = {lt2}')
#######################################################
print(f'{nn:#^60}')
n = ' range '
print(f'{n:#^60}')
#######################################################
lt4 = range(1,10)
print(lt4)
lt5 = list(range(1,10))
print(lt5)
#######################################################
print(f'{nn:#^60}')
#######################################################
soma=0
for valor in lt5:
    soma+=valor
print(soma)
#######################################################
print(f'{nn:#^60}')
#######################################################
lt6= ['String', True, 10, -20.5]
for el in lt6:
    print(f'O tipo de elem é {type(el)} e seu valor é {el}')
#######################################################
print(f'{nn:#^60}')
n = ' Forca '
print(f'{n:#^60}')
#######################################################
secreta = 'perfume'
digitado = []
contador = 0
while True:
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Apenas uma letra!!!')
        continue
    digitado.append(letra)
    if letra in secreta:
        print(f'Letra "{letra}" existe na palavra secreta')
    else:
        print(f'Letra "{letra}" NÃO existe na palavra secreta ')
        digitado.pop()
        contador += 1
    print(f'vc tem {3-contador} tentativas')
    #print(f'Lesta da palavra secreta: {digitado}')
    descoberto = ''
    for letra2 in secreta:
        if letra2 in digitado:
            descoberto += letra2
        else:
            descoberto += '_'
    print(descoberto)
    print()
    if descoberto == secreta:
        print(f'vc consegui resolver a palavra secreta "{descoberto}"')
        break
    if contador >= 3:
        print(f'Perdeu a palavra secreta era "{secreta}"')
        break
#######################################################
print(f'{nn:#^60}')
#######################################################
#######################################################
print(f'{nn:#^60}')
n = ' Existe Letra? '
print(f'{n:#^60}')
#######################################################
v = ['Davi', 'karine', 'Sofia']
c = False
for a in v:
    if a.lower().startswith('s'):
        c = True
if c == True:
    print('Existe palavra com "s"')
else:
    print('Não existe palavra com "s"')

for a in v:
    if a.lower().startswith('s'):
        print('Existe palavra com "s"')
        break
else:
    print('Não existe palavra com "s"')

for a in v:
    if a.lower().startswith('s'):
        continue
    print(a)
#######################################################
print(f'{nn:#^60}')
n = ' Desempacotamento '
print(f'{n:#^60}')
#######################################################
'''
Desempacotamento de lista e python
'''
lista = ['davi', 'karine', 'sofia', 1, 2, 3, 4, 5]
n1, n2, n3, *n4, n5, n6 = lista
m1, m2, *m = lista
print(n1, n4, n6)
print(m1, m2)


#######################################################
print(f'{nn:#^60}')
n = ' Tuplas '
print(f'{n:#^60}')
#######################################################
#  muitos parecidas de lista, mas não pode ser alteradas
t1 = ()
print(type(t1))
t2 = (1, 2, 3, 'davi', 'Sofia')
print(t2)
t3 = 1,
print(type(t3))
t4 = (1, 2, 3, 4, 5)
t4 = list(t4)
t4[1] = 3000
t4 = tuple(t4)
print(t4)

#######################################################
print(f'{nn:#^60}')
n = ' Dicionario '
print(f'{n:#^60}')
#######################################################
d1 = {'chave1':'valor da chave'}
print(d1)



#######################################################
print(f'{nn:#^60}')
n = ' Dicionario '
print(f'{n:#^60}')
#######################################################
# dicionario muito similar as listas
d1 = {'chave1':'valor da chave'}
print(d1)
d1['nova_chave'] = 'Valor da nova chave'
print(d1)
d2 = dict(chave1='valor da chave', chave2 = 'valor da outra chave')  # formato menos utilizado par criar dicionario
d2['nova_chave'] = 'Valor da nova chave'
print(d2)
d3 = { 'chave': 1, 'chave': 2, 'chave': 3}
print(d3)
d4 = {'str': 'davi', 123: 'inteiro diferentes', (1, 2, 3, 4): 'tupla'}
print(d4[(1, 2, 3, 4)])
print('str' in d4)
print('str' in d4.keys())
print('davi' in d4.values())
print(len(d4))

for k in d4:
    print(f'só d4:                  {k}')
for k in d4.values():
    print(f'd4.values:              {k}')
for k in d4.items():
    print(f'd4.items:               {k}')
    print(f'k[0], k[1]:             {k[0], k[1]}')
for k, v in d4.items():
    print(f'k, v:                   {k, v}')

clientes = {
    'cliente1' : {
        'nome' : 'Davi'
        ,'sobrenome' : 'Pinheiro'
    }
    ,'cliente2' : {
        'nome' : 'karine'
        ,'sobrenome' : 'Pinto'
    }
    , 'cliente3': {
        'nome': 'Sofia'
        , 'sobrenome': 'Pedreira'
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'O cliente: {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')


x = {1:'a', 2:'b', 3:'c'}
print(f'valor de x inicial é:   {x}')
y = x  # indica o mesmo objeto não criar um novo objeto
w = x.copy()
import copy
k = copy.deepcopy(x)  # faz uma copia
y[1]='y'
w[2]='w'
k[3]='k'
print(f'valor de x é:           {x}')
print(f'valor de y é:           {y}')
print(f'valor de w é:           {w}')
print(f'valor de k é:           {k}')
k.pop(2)  #remover o elemento
print(f'valor de k.pop(2):      {k}')
k.popitem()  #elimia o ultimo item
print(f'valor de k.popitem():   {k}')   #  obs ira substituir a chave 1 pois tem tambem no x
k.update(x)
print(f'valor de k.update(x)    {k}')

z=list(y)
z[1]='e'  # obs: quando se tratar de lista o que tiver entre [] vai ser o índice
print(f'valor de z é:           {z}')


lista = [
    [1, 'a'],
    [2, 'b'],
    [3, 'c']
]
dicionario = dict(lista)
print(dicionario)

tupla = (
    (1, 'a'),
    (2, 'b'),
    (3, 'c')
)
dicionario = dict(tupla)
print(dicionario)

tupla_lista = (
    [1, 'a'],
    [2, 'b'],
    [3, 'c']
)
dicionario = dict(tupla_lista)
print(dicionario)


#######################################################
print(f'{nn:#^60}')
n = ' sistema de pergunstas e resposta utilizando dicionario '
print(f'{n:#^60}')
#######################################################
print()
print('Texto explicativo')

p = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'escolhas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3x2? ',
        'escolhas': {
            'a': '4',
            'b': '101',
            'c': '6',
        },
        'resposta': 'c',
    },
}
print()

respostas_certas = 0
for x, y in p.items():
    print(f'{x}: {y["pergunta"]}')
    print('########################')
    for z, w in y['escolhas'].items():
        print(f'({z}) {w}')
    resposta_usuario = input('Qual o item correto? : ')
    if resposta_usuario == y['resposta']:
        print('Certo')
        respostas_certas += 1
    else:
        print('Errado')

    print()

quantidade_perguntas = len(p)
porcentagem_acerto = respostas_certas / quantidade_perguntas * 100
print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%.')

#######################################################
print(f'{nn:#^60}')
n = ' sets '
print(f'{n:#^60}')
#######################################################
s1 = {1,2,3,4,5}   # igua a criacao de dicionario mas nao existe referencia e não tem indice não tem como acessar o valor diretamente
for i in s1:
    print(i)
d1={}   # é um dicionari vazio
s2 = set()  # é um sets vazio
print(s2)
s2.add(1)
s2.add(2)
print(s2)
s2.add((1,2,3,'Davi'))
print(s2)
s2.discard(2)
print(s2)
s2.update('Python')  # não aceita ordem
print(s2)

l1 = [1,2,3,1,1,1,1,1,'davi','davi',4,3,2,4,5]
s3 = set(l1)  #remove os duplicados
print(s3)
l1 = list(s3)  # problema que pode esta fora de ordem
print(l1)

s4 = {1,2,3,4,5}
s5 = {2,3,4,5,6}
s6 = s4 | s5
s7 = s4 & s5
s8 = s4 - s5
s9 = s5 - s4
s10 = s4 ^ s5
print(f's4 | s5 {s6}. s4 & s5 {s7}. s4 - s5 {s8}. s5 - s4 {s9}. s4 ^ s5 {s10}')
print(s7)

#######################################################
print(f'{nn:#^60}')
#######################################################