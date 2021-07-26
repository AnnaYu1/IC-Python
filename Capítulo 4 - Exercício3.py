#programa que leia um conjunto de números (termos) do teclado e imprima o produto de todos esses números

numtermos=0
numtermos=int(input("Entre com o numero de termos: "))
lista = []
produto=1
aux=0

if numtermos == 0:
    print ("zero")
for i in range (numtermos):
    termo=int(input("Digite aqui o valor dos termo " + str(i+1)+':'))
    lista.append(termo)
    
for i in range (len(lista)):
    aux=lista[i]
    produto*= aux

print (lista)
print ('Produto dos termos:',produto)

