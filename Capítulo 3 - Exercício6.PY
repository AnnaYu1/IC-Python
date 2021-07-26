
#programa que calcule a média final de um aluno da matéria de Abstração I da Universidade da Bachatóvia.
    
p1= float(input('Digite o valor da prova 1: '))
p2= float(input('Digite o valor da prova 2: '))

M=(p1+p2)/2

if M>=7:
    print('Aprovado, média final: ', M)

elif M<3:
    print('Reprovado, média final: ', M)

elif 3<M<7:
    print('Prova final')
    pf=float(input('Digite o valor da prova final'))
    MF=(M+pf)/2
             
    if MF>=5:
        print('Aprovado, média final: ', MF)
        print('Parabéns!')

    elif MF<5:
        print('Reprovado, média final: ', MF)
                 

        
    
             
            
             

          
    
          

    
        



 
    
    
    




  

    

    
    


 

    
    
    
