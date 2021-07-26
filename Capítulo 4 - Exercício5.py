#Exercício 5 capítulo 4

numeros=[]
contador=0
contador2=0
k=1
inserir=0
while inserir >= 0:
    inserir=int(input('Digite aqui o número '+str(k)+' do conjunto: '))
    k+=1
    numeros.append(inserir)
for i in range(len(numeros)):
    contador+=1
    if numeros[i]%10==0:
        print('Existe mútiplo de 10 neste conjunto')
        break
    else:
        contador2+=1
if contador2==contador:
    print('Não existe um multiplo de 10 neste conjunto')
    
