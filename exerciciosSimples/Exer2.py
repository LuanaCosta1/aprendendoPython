
print ('Programa para verificar aprovação de alunos')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2
provaRec = 0

if (media < 6 and media > 1):
    print ('Esse aluno teve que fazer AF.')
    provaRec=float(input('Digite a nota da prova de recuperação: '))

if(media >= 6 or provaRec >= 6):
    print ('Aprovado.')
else:
    print ('Reprovado.')

print ('A sua média é: ', media)
print ('ProvaRec: ', provaRec)

print('FIM ============================================================================')
