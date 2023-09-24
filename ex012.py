from datetime import datetime
dicionario = dict()
dicionario['Nome'] = str(input('Qual seu nome: '))
anoNascimento = int(input('Qual no de nascimento: '))
dicionario['Idade'] = (datetime.now().year - anoNascimento)
dicionario['CTPS'] = int(input('Carteira de Trabalho: (0 não tem) '))
if dicionario['CTPS'] != 0:
    dicionario['AnoContratacao'] = int(input('Ano de contratação: '))
    dicionario['Salario'] = float(input('Salário: R$'))
    dicionario['Aposentadoria'] = (dicionario['AnoContratacao'] + 35) - anoNascimento
print('-='*20)
for i, e in dicionario.items():
    print(f' - {i}: {e}')