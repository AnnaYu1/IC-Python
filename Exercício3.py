#programa em python que leia os horários de partida e chegada do trem e informe:
#1- o tempo total de viagem

H1= int(input('hora da partida: '))
M1= int(input('minuto da partida: '))

H2= int(input('hora da chegada: '))
M2= int(input('minuto da chegada: '))

TH= (H2-H1)
MH= (M2-M1)
if(MH<0):
    MH=60+MH
    TH=TH-1

print('O trem partiu as', H1,':', M1)
print('O trem chegou as', H2, ':', M2)
print('Tempo de viagem:', TH,':', MH)

    
