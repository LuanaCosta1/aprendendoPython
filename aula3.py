a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))
media = (a + b + c + d)/4

if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('media: {}' .format(media))
else: print('Nota inválida! Tente novamente')
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print('o maior número é {}.' .format(a))
# elif b > a and b > c:
#     print('o maior número é {}' .format(b))
# elif c > a and c > b:
#     print('o maior número é {}' .format(c))
# else:
#     print('Números iguais.')
# print('Final do programa')
