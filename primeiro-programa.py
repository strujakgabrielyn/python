import random
num_oculto = random.randint(0,100)
tentativas = 10
ltentativas = []

print('︽'*50)
j = 'JOGO NÚMERO OCULTO'
print('\033[1;35m {:>40}\033[m'.format(j))
print('︾'*50)
print('\033[1;35mBem vindo ao jogo do número oculto!\nDesafio você a acertar o número oculto!\033[1;33m(Dica: 0 a 100)\033[m')

while tentativas > 0:
    n= int(input('Adivinhe o número oculto:'))
    print('')
    if n not in (ltentativas):
     ltentativas.append(n)
    else:
     print(f'Você já fez esta tentativa, tente outra vez! Você tem {tentativas} tentativas restantes.')
     continue
    if n == num_oculto:
        print(f'\033[1;32mParabéns, você acertou! O número oculto era {num_oculto}.\033[m')
        print('')
        break
    else:
        if n > num_oculto:
            print('Tente um número menor!', end='')
        elif n < num_oculto:
            print('Tente um número maior! ', end='')

    tentativas -= 1
    print(f'Você tem {tentativas} tentativas restantes.')

print('\033[1;33m︿\033[m'*15)
ltentativas.sort()
print(f'A menor tentativa foi: {ltentativas[0]}\nA maior tentativa foi: {ltentativas[-1]}')
print('\033[1;33m﹀\033[m'*15)

print('︽'*50)
f = 'FIM DO JOGO'
print('\033[1;35m{:>40}\033[m'.format(f))
print('︾'*50)

mozinhoevzy
