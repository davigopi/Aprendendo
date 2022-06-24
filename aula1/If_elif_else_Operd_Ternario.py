nn = '#'
#######################################################
print(f'{nn:#^60}')
n = ' Condição '
print(f'{n:#^60}')
#######################################################
"""
Condições IF, ELIF e ELSE - Aula 4
"""
if False:
    print("Verdadeiro.")

elif True:
    num_1 = 2
    num_2 = 4

    print(num_1+num_2)
else:
    print('Falso')

print(f'{nn:#^60}')

#######################################################
print(f'{nn:#^60}')
n = ' Saber a condição corporal da pessoa '
print(f'{n:#^60}')
#######################################################
"""
variaveis: Iniciar com letra, pode conter números, nome composto seprar _, letras minúsculas
"""
nome = 'Davi'
idade = 39
altura = 1.94
e_maior = idade > 18
peso = 128
imc = peso/(altura**2)
ano_atual = 2022
nascimento = ano_atual - idade

if imc >= 40:
    resultado = 'Obesidade III'
elif imc >=35:
    resultado = 'Obesidade II'
elif imc >= 30:
    resultado = 'Obesidade I'
elif imc >= 25:
    resultado = 'Acima do peso(Sobrepeso)'
elif imc >= 18.5:
    resultado = 'Peso normal'
else:
    resultado = 'Abaixo do peso'

print(f'{nome} tem {idade} anos de idade e seu imc é: {imc:.3f} você é considerado : {resultado} e nasceu em {nascimento} ')
print('{} tem {} anos de idade e seu imc é: {:.3f} você é considerado : {}'.format(nome, idade, imc, resultado))
print('{0} tem {1} anos {1} de idade e seu imc é: {2:.3f} você é considerado : {3}'.format(nome, idade, imc, resultado))
print('{id} tem {n} anos de idade e seu imc é: {i:.3f} você é considerado : {r}'.format(n=nome, id=idade, i=imc, r=resultado))
print('para sua altura a faixa a baixo do peso é menor que:', round(18.499*altura**2,3))
print('para sua altura a faixa normal é até:', round(18.5*altura**2,3), 'até:', round(24.999*altura**2,3))
print('para sua altura a faixa de sobre peso é:', round(25*altura**2,3), 'até:', round(29.999*altura**2,3))
print('para sua altura a faixa de obsidade I é:', round(30*altura**2,3), 'até:', round(34.999*altura**2,3))
print('para sua altura a faixa de obsidade II é:', round(35*altura**2,3), 'até:', round(39.999*altura**2,3))
print('para sua altura a faixa de obsidade III é maior que:', round(40*altura**2,3))


#######################################################
print(f'{nn:#^60}')
n =' Simplificar '
print(f'{n:#^60}')
#######################################################

nome = input('Qual o seu nome? ')
if nome:
    print(nome)
else:
    print('Você não digitou nada =( ')
n = ' Iguais funçoes porem mais simples '
print(f'{n:#^60}')
print(nome or 'Você não digitou nada =( ')

a = 0
b = None
c = False
d = {}
e = []
f = 28
g = 'Davi'
variavel = a or b or c or d or e or f or g
print (variavel)

#######################################################
print(f'{nn:#^60}')
n = ' Operadores ternário '
print(f'{n:#^60}')
#######################################################
'''
Operador ternário em python
'''

logged_user = False
if logged_user:  # = if logged_user == True
    msg = 'Usuário logado'
else:
    msg = 'Usuário não logado'
print(msg)

#######################################################
print(f'{nn:#^60}')
n = ' = + utiliza operadores ternário '
print(f'{n:#^60}')
#######################################################

msg = 'Usuário logado' if logged_user else 'Usuário não logado'
print(msg)

#######################################################
print(f'{nn:#^60}')
#######################################################

idade = input ('Qual sua idade: ')
if not idade.isnumeric():
    print('Vc precisa digitar apenas numero')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar'
    print(msg)


#######################################################
print(f'{nn:#^60}')
