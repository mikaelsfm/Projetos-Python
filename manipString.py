#1-
#str1 = input('Primeira String: ')
#str2 = input('Segunda String: ')
#
#print ('*'*10)
#print(f'String 1: {str1}')
#print(f'String 2: {str2}')
#contador = 0
#contador2 = 0
#for i in range(len(str1)):
#    contador += 1
#for j in range(len(str2)):
#    contador2 += 1
#print(f'Tamanho de "{str1}": {contador} caracteres.')
#print(f'Tamanho de "{str2}": {contador2} caracteres.')
#
#if contador != contador2:
#    print('As duas strings possuem tamanho diferente')
#if str1 != str2:
#    print('As duas strings possuem conteúdo diferente')

#2-
#tr = input('String: ')
#trcaps = str.upper()
#rint(strcaps)
#rint('Virando...')
#rint(strcaps[::-1])

#3-
#str = input('String: ')
#for i in range(len(str)):
#    print(str[i])

#4- e 5-
str = input('String: ')
for i in range (len(str)):
    print (str[0:i+1:])
for i in range (len(str)):
    print (str[::])