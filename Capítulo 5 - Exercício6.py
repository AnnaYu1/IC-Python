#Exercício 6 capítulo 4

gabarito=input("Entre com o gabarito: ")
questao=input("Entre com a resposta do aluno: ")

acertos = 0
resultado = 0
pontuacao= 0

for k in range (0,len(gabarito)):
    if questao[k] == gabarito[k]:
        pontuacao+=10 

print('A pontuação do aluno foi: ', pontuacao)
 
    
