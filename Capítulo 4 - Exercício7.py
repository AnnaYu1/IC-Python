#Exercício 7 capítulo 4

lista=[]
soma=0
media=0
quantidade=int(input('Digite aqui o número de notas a serem inseridas: '))
for i in range(quantidade):
    valor=float(input('Digite aqui a nota ' + str(i+1)+':'))
    lista.append(valor)
    soma+=valor
media=soma/quantidade
print('Esse foram todas as notas inseridas: ',(lista))
print('A sua média foi: ',(media))
if media >= (7.0):
    print('Aprovado com sucesso')
else:
    print('Parabéns, tente de novo ano que vem')
        
