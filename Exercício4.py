#programa em python que  leia um número inteiro entre 1 e 12 representando um mês e imprima se este mês tem 28, 30 ou 31 dias

Vetor1=[1,3,5,7,8,10,12]
Vetor2=[4,6,9,11]
Vetor3=[2]

mes=int(input('digite o numero do mes: '))
if(mes  in (Vetor1)):
    print('Mes com 31 dias')

elif(mes in (Vetor2)):
    print('mes com 30 dias')

elif(mes in (Vetor3)):
    print('mes com 28 dias')

else:
    print('mes invalido')

    
    
    
