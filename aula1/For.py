"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)

# continue - pula para o proximo laço
# break - termina o laço
"""
nn = '#'
#######################################################
print(f'{nn:#^60}')
n = ' Enumerar as letras '
print(f'{n:#^60}')
#######################################################

t = 'Python'
for n, letra in enumerate(t):
    print(n, letra)
#######################################################
print(f'{nn:#^60}')
n = ' Contador do inicio 2 at 50 em 7 e 7 '
print(f'{n:#^60}')
#######################################################

for n in range(2, 50, 7):
    print(n)

#######################################################
print(f'{nn:#^60}')
n = ' while = for '
print(f'{n:#^60}')
#######################################################

print(f'{nn:#^60}')

a=0
while a <len(texto):
    print(texto[a])
    a+=1

print('Sao iguais')

for letra in texto:
    print(letra)

#######################################################
print(f'{nn:#^60}')
n = ' break no for '
print(f'{n:#^60}')
#######################################################

t2 = ''
for letra in t:
    if letra == 'y':
        t2+=letra.upper()
    elif letra == 'h':
        t2+=letra.upper()
        break
    else:
        t2+=letra
print(t2)

#######################################################
print(f'{nn:#^60}')
