n1 = float(input('Qual a sua primeira nota?'))
n2 = float(input('Qual a sua segunda nota?'))
m = (n1+n2)/2
print('A sua média foi {}' .format(m))

if m>=6:
    print('Arrasou na nota! Parabéns :)')
else:
    print('Eita! Precisa estudar mais :(')