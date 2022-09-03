# print('Olá Mundo !')

# nome = input('Qual é seu nome?')
# print('É um prazer te conhecer', nome) #.format(nome)

# n1 = int(input('Digite um valor:'))
# n2 = int(input('Digite outro valor:'))
# s = n1+n2
# print('A soma entre {} e {} é igual a {}' .format(n1,n2,s))

# ava = input('Digite algo:')
# print('O tipo primitivo desse valor é', type(ava))
# print('É um numero?', ava.isnumeric())
# print('É alfabetico?', ava.isalpha())
# print('É alfanumerico?', ava.isalnum())
# print('Está em maiscula', ava.isupper())
# print('Está em minuscula?', ava.islower())
# print('Esta capitalizado?', ava.istitle())

# s = int(input('Digite um numero:'))
# print ('Analisando o valor {}, o seu sucessor será {} e seu antecessor será {}' .format(s,(s+1),(s-1)))

# s = int(input('Digite um número:'))

# print('O dobro desse número será:{}' .format(s*2))
# print('O triplo desse número será:{}' .format(s*3))
# print('A raiz quadrada desse número é:{:.2f}' .format(s ** (1/2)))

# n1 = float(input('Digite a primeira nota:'))
# n2 = float(input('Digite a segunda nota:'))


# print('A sua média é : {}' .format((n1+n2)/2))

# metros = int(input('Digite a medida em metros:'))

# print(' {}m é igual a {}cm e {}mm' .format(metros,(metros*100),(metros*1000)))

# from math import trunc

# num = float(input('Digite um valor:'))

# print('O valor digitado foi {} e sua porção inteira é {}' .format(num, trunc(num)))

# num = int(input('Digite um valor:'))

# print('O valor do SENO:')
# print('O valor do COS:')
# print('O valor do TANG:')

n1 = float(input("Digite a sua nota:"))
n2 = float(input("Digite a sua nota:"))

m = (n1+n2) / 2

print("A sua média foi de {}" .format(m))

if m>=6:
    print("Parabens! Você foi aprovado")
else:
    print("Precisa estudar mais ! Reprovado")

