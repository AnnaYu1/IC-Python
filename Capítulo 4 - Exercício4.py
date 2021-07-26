

i=0
num=int(input('Entre com o número '+str(i+1)+' do conjunto: '))
multiplos=set()
while(num >1):
    multiplos.add(num)
    if (num%10>=0):
        print('Existem múltiplos de 10')
        if num<0:
            break

else:
    print('Não existem múltiplos de 10')
