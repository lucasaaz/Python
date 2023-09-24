def soma(a, b):
    s = a + b
    print(s)

def soma_varios(*num):
    soma = 0
    for i in num:
        soma += i
    print(soma)

def soma_varios2(Lista):
    #Metodo reduzido
    s = 0
    for i in Lista:
        s += i
    print(s)
    #Metodo normal
    cont = soma = 0
    for i in Lista:
        soma += Lista[cont]
        cont += 1
    print(soma)


#Programa principal
a = int(input('Digite 1° numero: '))
b = int(input('Digite 2° numero: '))
soma(a, b)
soma_varios(21, 29, 50)
soma_varios(1, 1, 1, 1, 1)
lts = [41, 59, 100]
LTS = [2, 2, 2, 2, 2]
soma_varios2(lts)
soma_varios2(LTS)
