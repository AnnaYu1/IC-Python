xc=int(input('Digite a coordenada x do centro do circulo: '))
yc=int(input('Digite a coordenada y do centro do circulo: '))
r=int(input('Digite o raio do circulo: '))

x=int(input('Digite a coordenada x do ponto de teste: '))
y=int(input('Digite a coordenada y do ponto de teste: '))

if (x-xc)**2+(y-yc)**2==r**2:
    print('Ponto de teste está na fronteira')

elif (x-xc)**2+(y-yc)**2>r**2:
    print('Ponto de teste está fora do circulo')

elif (x-xc)**2+(y-yc)**2<r**2:
    print('Ponto de teste está dentro do círculo')

elif xc-yc==x-y:
    print('ponto de teste está dentro do circulo')
    
        
      

      
