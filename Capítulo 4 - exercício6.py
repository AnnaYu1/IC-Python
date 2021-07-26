#Exercício 6 (4.5)

lista=[]
contador=0
quantidade=int(input('Digite aqui o número de coordenadas a serem inseridas: '))
for i in range(quantidade):
    valor=float(input('Digite aqui a coordenada a ser inserida'+ str(i+1)+':'))
    lista.append(valor)
for i in range(len(lista)):
    if (lista[i])<0:
        print('Este vetor não se encontra no primeiro ortante')
        break
    else:
        contador+=1
if contador == quantidade:
    print ('Este vetor se encontra no primeiro ortante')
print(lista)
