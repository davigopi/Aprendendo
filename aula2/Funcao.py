nn = '#'
#######################################################
print(f'{nn:#^60}')
n = ' FUNCOES '
print(f'{n:#^60}')
#######################################################
'''
Funçes - def em python (parte 1)
'''
def funcao1():
    print('Olá mundo')

funcao1()
funcao1()
######################################################
n = ' FUNCAO2 '
print(f'{n:#^60}')
######################################################
def funcao2(msg, nome):
    print(msg, nome)
funcao2('mensgem', 'Davi')
funcao2('oi', 'Sofia')
######################################################
n = ' FUNCAO3 '
print(f'{n:#^60}')
######################################################
def funcao3(msg='ola', nome='karine'):
    msg = msg.replace('o', ':)')
    print(msg, nome)
funcao3('oi', 'Sofia')
funcao3()
funcao3('bom dia')
funcao3(nome='Samuel')
funcao3(nome='Marina', msg='tudo bem')
######################################################
n = ' FUNCAO4 '
print(f'{n:#^60}')
######################################################
def funcao4(msg='ola', nome='karine'):
    msg = msg.replace('o', ':)')
    print(msg, nome)
    return f'{msg} {nome}'
variavel = funcao4()
print(variavel)
######################################################
n = ' FUNCAO5 '
print(f'{n:#^60}')
######################################################
def funcao5(var):
    print(var)
variavel = funcao5('Valor que eu quero')
print(variavel)
######################################################
n = ' FUNCAO6 a baixo tem return '
print(f'{n:#^60}')
######################################################
def funcao6(var):
    print(var)
    return var
    # print('Não sera executado')
variavel = funcao6('Valor que eu quero')
print(variavel)
######################################################
n = ' divisao '
print(f'{n:#^60}')
######################################################
def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2
divide = divisao(8, 0)
if divide:
    print(divide)
else:
    print('Conta inválida')
######################################################
n = ' DUMP1 '
print(f'{n:#^60}')
######################################################
def dump1():
    return [1, 2, 3, 4, 5]
var = dump1()
print(var, type(var))
######################################################
n = ' FUNCAO7 '
print(f'{n:#^60}')
######################################################
def funcao7(var):
    print(f'{var} funcao')
def dump2():
    return funcao7
var = dump2()
print(type(var), id(var), id(funcao7))

var('var é iguala a')
######################################################
n = ' dump3 '
print(f'{n:#^60}')
######################################################
def dump3():
    return('Davi', 'Pinheiro')
var = dump3()
print(var[1], type(var))
######################################################
n = ' FUNC1 '
print(f'{n:#^60}')
######################################################
def func1(a1, a2, a3, a4, a5, nome=None, a6=None):  # depoois que definiu uma vez tem que definir o restante
    print(a1, a2, a3, a4, a5, nome, a6)

var = func1(1, 2, 3, 4, 5, nome='Davi', a6='6')  # depois que enviou um como parametro tem que enviar o restante
print(var)

######################################################
n = ' FUNC2 '
print(f'{n:#^60}')
######################################################
lista = [1, 2, 3, 4, 5]
n1, n2, *n = lista
print(n1, n2, n)
print(*lista, sep=' - ')

def func2(*n):
    print(n)
    print(n[0])
    print(n[-1])
    print(len(n))
    for v in n:
        print(v)
    n = list(n)  # converter em lista vai de () para []
    n[0] = 20
    print(n)
func2(1, 2, 5, 7, 9)

######################################################
n = ' FUNC3 '
print(f'{n:#^60}')
######################################################
def func3(*x):
    print(x)
    print(x[0])
    print(x[-1])
    print('############')
l = [1, 3, 5, 7, 9]
l2 = [21, 25]
func3(l, 11, 12, l2)
func3(*l, 11, 12, *l2)  # o * envia lista desempacotada

######################################################
n = ' FUNC4 '
print(f'{n:#^60}')
######################################################
def func4(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['nome'], kwargs['sobrenome'])
    nome = kwargs.get('nome')
    print(nome)
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print('idade nao existe')
    sobrenome = kwargs.get('sobrenome')
    if sobrenome is not None:
        print(sobrenome)
    else:
        print('sobrenome nao existe')

func4(*l, *l2, nome='Davi', sobrenome='Pinheiro')
######################################################
n = ' FUN1 FUN2 FUN3 FUN4 atilizacao de variaveis '
print(f'{n:#^60}')
######################################################
v = '1'
def fun1():
    print(v)
def fun2():
    v = '2'
    print(v)
def fun3():
    global v  # nao é boa pratica na programação
    v = '3'
    print(v)
def fun4(arg=None):
    arg = int(arg) + 1
    return arg  # boa pratica

fun1()
fun2()
print(v)
fun3()
print(v)
v2 = fun4(arg=v)
print(v2)
######################################################
print(f'{nn:#^60}')
######################################################
