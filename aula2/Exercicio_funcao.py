nn = '#'
#######################################################
print(f'{nn:#^60}')
n = ' Saudacao '
print(f'{n:#^60}')
#######################################################
"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""


def saudacao(saud, nome):
    print(saud, nome)


saudacao('Olá', 'Davi')

#######################################################
print(f'{nn:#^60}')
n = ' professor '
print(f'{n:#^60}')


#######################################################

def saudacao(saudacao, nome):
    print(f'{saudacao} {nome}')


saudacao('Olá', 'Joãozinho')
saudacao('Oi', 'Maria')
saudacao('Hey', 'Eduardo')

#######################################################
print(f'{nn:#^60}')
n = ' Soma de tres números '
print(f'{n:#^60}')
#######################################################

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles.
"""
def soma(a, b, c):
    if a.isdecimal() and b.isdecimal and c.isdecimal():
        a = int(a)
        b = int(b)
        c = int(c)
        print(a + b + c)
    else:
        print('Não são números')

x = input('Digite 1º número: ')
y = input('Digite 2º número: ')
z = input('Digite 3º número: ')
soma(x, y, z)

#######################################################
print(f'{nn:#^60}')
n = ' professor '
print(f'{n:#^60}')
#######################################################

def soma(n1, n2, n3):
    print(n1 + n2 + n3)


soma(2, 1, 3)
soma(1, 1, 1)
soma(2, 1, 1)

#######################################################
print(f'{nn:#^60}')
n = ' Soma com seu percentual '
print(f'{n:#^60}')
#######################################################

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""
def somapercentual(a, b):
    if a.isdecimal() and b.isnumeric():
        a = int(a)
        b = float(b)
        return a + a * b/100
    else:
        return 'Erro no valor'
x = input('Digite um valor: ')
y = input('Digite um percentual: ')
z = somapercentual(x, y)
print(z)


#######################################################
print(f'{nn:#^60}')
n = ' professor '
print(f'{n:#^60}')
#######################################################

def aumento_percentual(valor, percentual):
    return valor + (valor * percentual / 100)


ap = aumento_percentual(50, 10)
print(ap)
ap = aumento_percentual(100, 10)
print(ap)
ap = aumento_percentual(10, 10)
print(ap)
ap = aumento_percentual(15, 100)
print(ap)

#######################################################
print(f'{nn:#^60}')
n = ' Fizz Buzz '
print(f'{n:#^60}')
#######################################################

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""

def fizzbuzz(a):
    if a.isdecimal():
        a = int(a)
        x = a % 3
        y = a % 5
        if x == 0 and y == 0:
            return 'FizzBuzz'
        if x == 0:
            return 'Fizz'
        if y == 0:
            return 'Buzz'
        return a
    else:
        return 'Você não diguitou um número'

b = input('Digite um numero par FizzBuzz: ')
c = fizzbuzz(b)
print(c)

#######################################################
print(f'{nn:#^60}')
n = ' professor '
print(f'{n:#^60}')
#######################################################

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzbuzz, {n} é divisível por 3 e 5'
    if n % 5 == 0:
        return f'buzz, {n} é divisível por 5'
    if n % 3 == 0:
        return f'fizz, {n} é divisível por 3'
    return n


from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))



nn='#'
#######################################################
print(f'{nn:#^60}')
n = ' funcao dentro de funcao '
print(f'{n:#^60}')
#######################################################
"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.
"""
def funcao1(func):
    return func()
def funcao2():
    return('Olá Mundo')
y = funcao1(funcao2)
print(y)



#######################################################
print(f'{nn:#^60}')
n = ' professor '
print(f'{n:#^60}')
#######################################################
def ola_mundo():
    return 'Olá mundo!'


def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo)
print(executando)


#######################################################
print(f'{nn:#^60}')
n = ' funcao recebe outra funcao != argumentos '
print(f'{n:#^60}')
#######################################################
"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número 
diferente de argumentos.
"""
def mestre(func, *args, **kwargs):
    return func(*args, **kwargs)
def f1(a, b):
    return f' O {a} é amigo de {b}'
def f2(x, y, z):
    v = f1(x, y)
    return f' ;) {v} e tambem de {z}'

v1 = mestre(f1, 'Davi','Samuel')
v2 = mestre(f2, 'Davi','Samuel',z ='Rafael')
print(v1)
print(v2)
#######################################################
print(f'{nn:#^60}')
n = ' professor '
print(f'{n:#^60}')
#######################################################
def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, 'Luiz', saudacao='Bom dia!')
print(executando)
print(executando2)
