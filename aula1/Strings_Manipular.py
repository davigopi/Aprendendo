nn = '#'
#######################################################
print(f'{nn:#^60}')
n = ' Quantidade de caracter '
print(f'{n:#^60}')
#######################################################

usuario = input('Digite seu usuário: ')
qtd_caract = len(usuario)

print(usuario, qtd_caract, type(qtd_caract))
if qtd_caract < 6:
    print('Voce precisa digitar pelo menos 6 caracteres')
else:
    print('voce diguito certo na quantidade de carcteres')

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade de caracter digitados foi {len(string1)+len(string2)}')
print(f'A quantidade de caracter digitados foi {string1.__len__()+string2.__len__()}')


#######################################################
print(f'{nn:#^60}')
n = ' Manipulação de Strings '
print(f'{n:#^60}')
#######################################################

"""
manipulando strings - aula 6
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funçoes podem ser usadas diretamente em cada tipo
"""

# poditivos     [012345678]
texto =         'Python_s2'
# negativos    -[987654321]
print(len(texto))

print( texto[7])
print( texto[2:6])  # 6 nao é incluido
print( texto[:6])
print( texto[2:])
print( texto[-1])
print( texto[:-1])
n = texto[0::3]
print(n)

#######################################################
print(f'{nn:#^60}')
#######################################################

#    indices
#    1234567..........................33
f = 'o rato roeu a roupa do rei de roma'
t=len(f)
c=0
c2=0
f2=''
print(f)
let=input('Da frase acima qual letra vc que maiúscula: ')

#######################################################
print(f'{nn:#^60}')
#######################################################

while c<t:
    #print(f[c], c)
    if f[c]==let:
        f2+=let.upper()
        c2+=1
    else:
        f2+=f[c]
    c+=1

print(f2)
print(f'Quantidade de letra {let.upper()} são: {c2}')

#######################################################
print(f'{nn:#^60}')
#######################################################

f2=''
for letra in f:
    if letra == let:
        f2+=let.upper()
    else:
        f2+=letra
print(f2)
print(f'Quantidade de letra {let.upper()} são: {c2}')

#######################################################
print(f'{nn:#^60}')
#######################################################


