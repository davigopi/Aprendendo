nn = '#'
#######################################################
print(f'{nn:#^60}')
n = ' Variaveis  '
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

if imc >= 40:
    resultado = 'Obesidade III'
else:
    if imc >=35:
        resultado = 'Obesidade II'
    else:
        if imc >= 30:
            resultado = 'Obesidade I'
        else:
            if imc >= 25:
                resultado = 'Acima do peso(Sobrepeso)'
            else:
                if imc >= 18.5:
                    resultado = 'Peso normal'
                else:
                    resultado = 'Abaixo do peso'

print(nome, 'tem', idade, ' anos de idade e seu imc é:', round(imc,3), 'você é considerado :', resultado)
print('para sua altura a faixa a baixo do peso é menor que:', round(18.499*altura**2,3))
print('para sua altura a faixa normal é até:', round(18.5*altura**2,3), 'até:', round(24.999*altura**2,3))
print('para sua altura a faixa de sobre peso é:', round(25*altura**2,3), 'até:', round(29.999*altura**2,3))
print('para sua altura a faixa de obsidade I é:', round(30*altura**2,3), 'até:', round(34.999*altura**2,3))
print('para sua altura a faixa de obsidade II é:', round(35*altura**2,3), 'até:', round(39.999*altura**2,3))
print('para sua altura a faixa de obsidade III é maior que:', round(40*altura**2,3))

#######################################################
print(f'{nn:#^60}')
n = ' = + de baixo código + simples '
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
elif imc >=35 :
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
n = ' Inverter variaveis '
print(f'{n:#^60}')
#######################################################
x = 10
y = 'Davi'
print(f'x={x} e y={y}')
z = x
x = y
y = z
print(f'x={x} e y={y}')
#######################################################
print(f'{nn:#^60}')
#######################################################
x = 10
y = 'Davi'
print(f'x={x} e y={y}')
x, y = y, x
print(f'x={x} e y={y}')