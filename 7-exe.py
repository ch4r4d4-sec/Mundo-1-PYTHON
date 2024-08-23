#FAÇA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO E CALCULE A MÉDIA.

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1 + nota2) / 2

print('Com base nas notas {} e {} sua média é {}' .format(nota1, nota2, media))