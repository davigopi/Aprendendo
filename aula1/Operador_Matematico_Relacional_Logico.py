nn = '#'
#######################################################
print(f'{nn:#^60}')
n = ' PAR ou IMPRA '
print(f'{n:#^60}')
#######################################################
'''
+, -, *, /,
//  divisao inteira aredondado
**  expodensiacao
%   retorna o modulo o resoto da divisao
()  alterar a presedencia da conta
'''
print('soma + ', 10 + 10)
print('cocatenacao + ', '10' + '10')
print('subtracoa - ', 10 - 10)
print('multiplicacao *', 10 * 10)
print('repeticao *', 10 * 'Davi')
print('divisao /', 10 / 10)
print('divisao interira 13//10 ', 13 // 10)
print('modulo 13%10', 13 % 10)
print('expodenssiacao 2**3', 2 ** 3)
print('precedencia 2*(2+2)', 2*(2+2))

'''
Opreradores Relacionais - Aula 4
== > >= < <= !=
'''
#######################################################
print(f'{nn:#^60}')
n = ' Opreradores Relacionais '
print(f'{n:#^60}')
#######################################################

variavel = 'valor'
print(2 == 2)
print(2 == 1)



"""
Operadores Lógicos
and, or, not
in e not in
"""
#######################################################
print(f'{nn:#^60}')
n = ' Opreradores Lõgicos '
print(f'{n:#^60}')
n = ' Comparacao1 and comparacoa2 '
print(f'{n:#^60}')
#######################################################

if not 3 > 2:
    print('é maior')
else:
    print('é menor')
print(f'{nn:#^60}')

nome= 'Davi Pinheiro'
letra='P'
if letra in nome:
    print(f'Existe {letra} no {nome}')
else:
    print(f'Não existe {letra} no {nome}')
print(f'{nn:#^60}')

usuario = input('nome de usuário: ')
senha = input('Senha do usuário: ')
us_bd = 'davi'
sh_bd = '123'
if usuario == us_bd and senha == sh_bd:
    print('Logado')
else:
    print('erro no usário ou senha')
    print(usuario)
    print(us_bd)
    print(senha)
    print(sh_bd)
print(f'{nn:#^60}')

#######################################################
print(f'{nn:#^60}')
#######################################################