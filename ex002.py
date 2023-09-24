notaAluno1 = int(input('Nota do aluno: '))
notaAluno2 = int(input('Nota do aluno: '))
notaAluno3 = int(input('Nota do aluno: '))

media = (notaAluno1+notaAluno2+notaAluno3) / 3

if notaAluno1>notaAluno2 and notaAluno1>notaAluno3:
    print('Maior nota Aluno1')
elif notaAluno2>notaAluno3:
    print('Maior nota Aluno2')
else:
    print('Maior nota Aluno3')
print(media)