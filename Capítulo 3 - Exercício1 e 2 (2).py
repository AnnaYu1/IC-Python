#programa em python que  leia um número inteiro entre 1 e 12 representando um mês e imprima se este mês tem 28, 30 ou 31 dias
def meses(mes):

    Vetor1=[1,3,5,7,8,10,12]
    Vetor2=[4,6,9,11]
    Vetor3=[2]

    if(mes  in (Vetor1)):
       return('Mes com 31 dias')

    elif(mes in (Vetor2)):
        return('mes com 30 dias')

    elif(mes in (Vetor3)):
        return('mes com 28 dias')

    else:
        return('mes invalido')


#programa que e leia um número inteiro positivo do teclado e informe se ele é par ou é ímpar     
def imparoupar(n):
    if n%2==0:
        return ("É par")
    else:
        return ("É impar")

#programa que leia os comprimentos dos lados de um triângulo e informe se o triângulo é equilátero, isósceles ou escaleno
    L1=input('Insira o primeiro lado: ')
    L2=input('Insira o segundo lado: ')
    L3=input('insira o terceiro lado: ')
       
if L1==L2==L3:
    return('equilátero')
if L1==L2!=L3:
    return('isosceles')
if L1==L3!=L2:
    return('isosceles')
if L2==L3!=L1:
    return('isosceles')
elif L1!=L2!=L3:
    return('escaleno')
        
    
    

    
    


 

    
    
    
