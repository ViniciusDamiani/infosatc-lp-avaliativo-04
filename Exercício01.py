#Crie uma função que receba uma palavra por parâmetro e permita inverter a ordem
#dessa palavra. Exemplo: ATOR = ROTA()

#Isso se chama Palíndromo, queria que a professorea usasse essa frase: Socorram me, subi no onibus em Marrocos
frase = str(input('Insira a Frase acima: '))
string = frase[::-1]
print('A frase que você digitou invertida fica: {}'.format(string))

print("----------------------------------------------")

def palindromo(text):
 result = "" 
 for i in text: 
   result = i + result
 return result 

print (palindromo ("A GRAMA É AMARGA"))