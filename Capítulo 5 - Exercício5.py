#Exercício 6 capítulo 5

numerotimes=int(input('Entre com o numero de times: '))
pontuacao=0
maiorpontuacao=0
campeao=''

for k in range(0,numerotimes):
     time=input('Entre com a string de resultados do time '+ str(k+1)+ ':')
     time=time.upper()
     for j in range(0,3
                    ):
         if time[j]== 'V':
             pontuacao+=3
         if time[j]== 'E':
             pontuacao+=1
     if pontuacao>maiorpontuacao:
         maiorpontuacao=pontuacao
         pontuacao=0

         campeao='Time '+ str(k+1)
print('Maior pontuacao: ', maiorpontuacao)
print('Campeao: ', campeao)
             
