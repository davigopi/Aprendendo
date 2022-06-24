"""
str-string
"""
print('aspas "dupla nao" simples')  # string
print("äspas 'simples nao' duplas")  # string
print("äspas \"simples nao\" duplas")  # \ caracter de escap
print('Esse e meu \n str')
print(r'Esse e meu \n str')
print(12345)  #numero


"""
tipos de dados primitivos
str - string -      'Assim' "Assim"
int - inteiro -     123   0   -10   -15000  1500 ....
float - real/ponto flutuante   -    12.3    0.0      10.0     -15000.1500
bool - booleano/logico   -    True/False   10==10
"""
print('Luiz', type('Luiz'))  # <class 'str'>
print(10, type(10))  # <class 'int'>
print(10.1, type(10.1))  # <class 'float'>
print(True, type(True))  # <class 'bool'>
print(10 == 'dez', type(10 == 'dez'))  # <class 'bool'>
print(10 == 10.0, type(10 == 10.0))  # <class 'bool'>
print(bool(''))  # <class 'bool'>
print(bool([]))  # <class 'bool'>
print(bool(0))  # <class 'bool'>
print('davi', type('davi'), bool('davi'))
print('10', type('10'), type(int('10')))
print('10'+'10')
print(10+10)
#####################################
"""
Entrada de dados - aula 3
"""
nome = input('Qual o seu nome? ')  # input retorna string
idade = input('Qual o sua idade? ')
idade = int(idade)
nascimento = 2022 - idade
print()
print(f'O usuário digitou {nome}, o tipo da variável é {type(nome)}  '
      f'e tem a idade {idade} e nacesceu em {nascimento}')


#####################################
#   Checar
n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

# isnumeric isdigit isdecimal
# checa números e positivos
if n1.isdigit() and n2.isdecimal():
    n1 = int(n1)
    n2 = int(n2)
    print(n1 + n2)
else:
    print('Nao pude converter os números para realizar a conta')

