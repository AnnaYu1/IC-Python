#programa em python que calcule as duas raízes da equação de segundo grau e le os valores:
#1- a
#2- b
#3- c

a= complex(input('Entre com o valor de a: '))
b= complex(input('Entre com o valor de b: '))
c= complex(input('Entre com o valor de c: '))


delta = b**2-4*a*c
R1= ((-b)+(delta)**(1/2))/(2*a)
R2= ((-b)-(delta)**(1/2))/(2*a)

print('Delta: ', delta)
print('R1: ', R1)
print('R2: ', R2)

