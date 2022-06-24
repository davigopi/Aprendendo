
nn = '#'
#######################################################
print(f'{nn:#^60}')
n = ' Enqunato for verdade  '
print(f'{n:#^60}')
#######################################################
"""
While em python - aula 7
utilizado para realizar acaoes enquanto
uma condicao for verdadeira

Requisitos entreder condicoes e operadores

# continue - pula para o proximo laço
# break - termina o laço

"""
a = True
while a == True:
    nome = input('qual seu nome? ')
    print(f'Olá {nome}')
    a = False
#######################################################
print(f'{nn:#^60}')
x = 0
while x < 5:
    print(x)
    x+=1
#######################################################
print(f'{nn:#^60}')
x = 0
while x < 5:
    if x == 3:
        x+=1
        continue  # ira pular o lup while
    print(x)
    x += 1
#######################################################
print(f'{nn:#^60}')
x = 0
while x < 5:
    if x == 3:
        x+=1
        break  # ira pular o lup while
    print(x)
    x += 1
#######################################################
print(f'{nn:#^60}')

x = 0  # coluna
y = 0  # linha
while x<5:
    y=0
    while y<4:
        print(f'({x},{y})')
        y+=1
    x+=1

#######################################################
print(f'{nn:#^60}')

a = True
while a == True:
    s = input('Vc que sair, se sim digite "(s)im": ')
    s = s.title()
    if s == 'S':
        #a = False
        break
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    op = input('Digite um operador: ')
    if not n1.isnumeric() or not n2.isnumeric():
        print('Vc precisa digitar um número!')
        continue
    n1=int(n1)
    n2=int(n2)
    if op == '+':
        print(n1+n2)
    elif op == '-':
        print(n1 - n2)
    elif op == '/':
        print(n1 / n2)
    elif op == '*':
        print(n1 * n2)
    else:
        print('vc precisa digitar um operador valido!')
#######################################################
print(f'{nn:#^60}')
n = ' Contador + Break '
print(f'{n:#^60}')
#######################################################
contador=1
acumulador=0
while contador<=10:
    acumulador = acumulador + contador
    if acumulador > 44:
        break
    print(contador, acumulador)
    contador+=1
else:
    print('cheguei no else')  # não passa devido ao break
print('#########################')
print('FIM')
print('#########################')

