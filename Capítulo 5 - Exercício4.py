#Exercício 4 capítulo 5

def frase():
    frase1 = input("escreva a primeira frase: ")
    frase2 = input("escreva a segunda frase: ")

    certo = 0

    for i in range(len(frase1)):
        if frase1[i] in frase2:
            certo += 1


    if certo == len(frase1):
        return "Todos os caracteres da primeira frase aparecem na segunda"

    else:
        return "Nem todos os caracteres da primeira frase aparecem na segunda "
