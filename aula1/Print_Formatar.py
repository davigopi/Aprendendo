nn = '#'
#######################################################
print(f'{nn:#^60}')
n = ' Print '
print(f'{n:#^60}')
#######################################################
"""
print('linha1')
print('linha2')
"""
# Uma linha
print('linha3')
# Outra linha
print('linha4')
print('linha5')  # isso é um comentario
print('linha6')


# print(123456)
# print('Davi', 'Pinheiro')
print('Davi', 'Pinheiro', sep='-', end='####')
print('Sofia', 'e', 'Pinheiro', sep='-')
# Print() não existe P maiusculo

"""
824.176.070-18
"""
print('824','176','070', sep='.', end='-')
print('18')

###########################################

"""
Formatar valores com módificadores - aula 5

:s - texto (strings)
:d - inteiros (int)
:f - números de ponto flutuante (float)
:.(NÚMREO)f - quantidade de casa decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerada
< - Direita
^ - Centro
"""
n1 = 10
n2 = 3
div = n1/n2
print(div)
print('{}'.format(div))
print('{:.2f}'.format(div))
print(f'{div:.2f}')
print(f'{div:0>10.2f}')
div = round(div,2)
print(f'{div:0>10}')
print(f'{n1:0>10}')

n = ' Davi Gomes pinheiro '
print(f'{n:s}')  # O s só informa que n é uma string
print(f'{n:#^60}')

n1=n.ljust(60, '#')
n2=n.lower()
n3=n.upper()
n4=n.title()
print(n1)
print(n2)
print(n3)
print(n4)