nn = '#'
#######################################################
print(f'{nn:#^60}')
n = ' PAR ou IMPRA '
print(f'{n:#^60}')
#######################################################

n = input('Digite um número inteiro: ')
if n.isdigit():
    n = int(n)
    parimpar = n % 2
    if n != 0:
        if parimpar == 0:
            print(f'O número {n} é PAR.')
        elif parimpar == 1:
            print(f'O número {n} é IMPAR.')
    else:
        print(' O 0 nao é par nem impar.')
else:
    print('Vc precisa digitar um número inteiro!')
#######################################################
print(f'{nn:#^60}')
n = ' COMPRIMENTAR '
print(f'{n:#^60}')
#######################################################

h = input('Que horas são: ')
if h.isdecimal():
    h = round(float(h), 2)
    if 0 <= h < 24:
        if h <= 12:
            print('Bom dia!!!')
        elif h < 18:
            print('Boa tarde!!!')
        else:
            print('Boa noite!!!')
    else:
        print('vc precisa digitar um horario entre 0 e 24 horas')
else:
    print('Vc precisa digitar um horá em número real!')
#######################################################
print(f'{nn:#^60}')
n = ' TAMANHO DO NOME '
print(f'{n:#^60}')
#######################################################
u = input('Digite o primeiro nome do usuário: ')
if not u.isdecimal():
    q = len(u)
    if q < 1:
        print('Vc precisa digitar seu nome!')
    elif q <= 1:
        print(f'Seu nome é curto. Só tem {q} caracter.')
    elif q <= 4:
        print(f'Seu nome é curto. Só tem {q} caracteres.')
    elif q <= 6:
        print(f'Seu nome é normal. Tem {q} caracteres.')
    else:
        print(f'Seu nome é grande. Tem {q} caracteres.')
else:
    print('Isso não é nome!')

#######################################################
print(f'{nn:#^60}')
n = ' CONTADOR '
print(f'{n:#^60}')
#######################################################

for x in range(9):
    print(x, 10-x)

#######################################################
print(f'{nn:#^60}')
n = ' Professor '
print(f'{n:#^60}')
#######################################################

for x, y in enumerate(range(10, 1, -1)):
    print(x, y)

#######################################################
print(f'{nn:#^60}')
n = ' CPF '
print(f'{n:#^60}')
#######################################################
cpf = input('Diguite um CPF, para validação: ')
# cpf = '168.995.350-19'
cpfforma = 'xxx.xxx.xxx-xx'
cpftemp = ''
cpfcompleto = ''
cpfcorreto = ''

if cpf.isdecimal() and len(cpf) == 11:
    cont = 0
    for x in cpfforma:
        if x == 'x':
            cpfcorreto += cpf[cont]
            cont += 1
        else:
            cpfcorreto += x.upper()
    cpf = cpfcorreto

cont = -1  # para ser igual ao indice
if len(cpf) == 14 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
    for x in cpf:
        cont += 1
        if x.isdecimal():
            cpfcompleto += x.upper()
        elif cont == 3 or cont == 7:
            continue
        elif cont == 11:
            cpftemp = cpfcompleto
        else:
            print(f' O CPF "{cpf}" errado. A forma correta é 012.345.678.90')
            cpftemp = False
            break

    if cpftemp:
        z = (10, 11)
        for y in z:
            resultado = 0
            for x in cpftemp:
                x = int(x)
                resultado += (x * y)
                y -= 1
            formula = 11 - (resultado % 11)
            if formula > 9:
                cpftemp += '0'
            else:
                cpftemp += str(formula)

        cont = 0
        cpfcorreto = ''
        for x in cpfforma:
            if x == 'x':
                cpfcorreto += cpftemp[cont]
                cont += 1
            else:
                cpfcorreto += x.upper()

        if cpftemp == cpfcompleto:
            print(f' O CPF "{cpfcorreto}" está correto')
        else:
            print(f' O CPF "{cpf}" está errado. Era para ser "{cpfcorreto}"')
else:
    print(f' O CPF "{cpf}" errado. A forma correta é 012.345.678.90')

#######################################################
print(f'{nn:#^60}')
n = ' CPF do professor '
print(f'{n:#^60}')
#######################################################

"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

# Loop infinito
#while True:
# cpf = '16899535009'
cpf = input('Digite um CPF: ')
novo_cpf = cpf[:-2]                 # Elimina os dois últimos digitos do CPF
reverso = 10                        # Contador reverso
total = 0

# Loop do CPF
for index in range(19):
    if index > 8:                   # Primeiro índice vai de 0 a 9,
        index -= 9                  # São os 9 primeiros digitos do CPF

    total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

    reverso -= 1                    # Decrementa o contador reverso
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:                   # Se o digito for > que 9 o valor é 0
            d = 0
        total = 0                   # Zera o total
        novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

# Evita sequencias. Ex.: 11111111111, 00000000000...
sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

# Descobri que sequências avaliavam como verdadeiro, então também
# adicionei essa checagem aqui
if cpf == novo_cpf and not sequencia:
    print('Válido')
else:
    print('Inválido')

#######################################################
print(f'{nn:#^60}')
n = ' CPF gerador do professor '
print(f'{n:#^60}')
#######################################################
from random import randint
numero = str(randint(100000000, 999999999))

novo_cpf = numero                   # 9 números aleatórios
reverso = 10                        # Contador reverso
total = 0                           # O total das multiplicações

# Loop do CPF
for index in range(19):
    if index > 8:                   # Primeiro índice vai de 0 a 9,
        index -= 9                  # São os 9 primeiros digitos do CPF

    total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

    reverso -= 1                    # Decrementa o contador reverso
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:                   # Se o digito for > que 9 o valor é 0
            d = 0
        total = 0                   # Zera o total
        novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

print(novo_cpf)


########################################################
print(f'{nn:#^60}')
