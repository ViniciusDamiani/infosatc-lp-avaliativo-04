#Crie uma função que receba por parâmetro DUAS palavras e verifique se uma é o
#inverso da outra.

def verificar (palavraIncial,palavraInversa):
    if palavraInversa == palavraIncial [::-1]:
        return True 
    else:
        return False

palavraIncial = input("Informe o nome a ser verificado: ") 
palavraInversa = input ("Informe o nome ao contrário para verificar: ") 
verificando = verificar (palavraInversa,palavraIncial)
print (verificando)