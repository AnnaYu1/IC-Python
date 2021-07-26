#Exercício 2 capítulo 5

frase= input("Digite sua frase: ")
resposta= frase[0]

if resposta[0]==str.upper(resposta[0]):
    resposta = str.lower(resposta)

elif resposta[0]==str.lower(resposta[0]):
    resposta = str.upper(resposta)

#print(resposta)
for i in range(1, len(frase)):
    if frase[i]==str.upper(frase[i]):
        resposta = str(resposta) + str.lower(frase[i])

    else:
        resposta = str(resposta) + str.upper(frase[i])

print(resposta)
    
