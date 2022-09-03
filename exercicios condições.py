# Exercício 28
# import random

# x = random.randint(0,5)
# s = int(input("Escolha um numero de 0 a 5: "))
# if x == s:
    #print("Parabens, você acertou")
# else:
    #print("Errou, tente novamente")
# print('--FIM--')

# Exercício 29

# s = int(input("Digite a velocidade do veiculo: "))

# esc = s - 80
# mul = esc * 7

# if s>80:
    # print('Você recebeu uma multa! O valor foi de: R${}' .format(mul))


# Exercício 30
# x = int(input('Digite um número: '))

# s = x % 2
# if s==0:
#    print(' É PAR ')
#    print('--FIM--')

# else:
#    print('É IMPAR')
#    print('--FIM--')

# Exercício 31
# x = int(input('Qual a distância da viagem? '))
# ct = x * 0.50
# lg = x * 0.45
# if x>200:
#    print('Considerando o KM que será percorrido o valor a ser pago é de: R$', lg)
# else:
#    print('Considerando o KM que será percorrido o valor a ser pago é de: R$', ct)

# Exercício 32

# a = int(input('Digite uma valor:'))
# b = int(input('Digite uma valor:'))
# c = int(input('Digite uma valor:'))

# if a > b > c:
#    print('O maior valor é', a)
# if b > a > c:
#    print('O maior valor é', b)
# if c > b > a:
#    print('O maior valor é', c)

# if a < b < c:
#    print('O menor valor é', a)
# if b < a < c:
#    print('O menor valor é', b)
# if c < b < a:
#    print('O menor valor é', c)

# Exercício 32:

# sal = int(input('Qual é seu salário:'))

# n1 = (0.10*sal) + sal
# n2 = (0.15*sal) + sal

# if sal>1250:
#    print('O valor do reajuste será de: R${:.2f}' .format(n1))
# else:
#    print('O seu novo salário é de : R${:.2f}' .format(n2))

# Exercício 33

a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))

if a < b + c and b < a + c and c < a + b:
    print('verdade')
else:
    print('falso')













