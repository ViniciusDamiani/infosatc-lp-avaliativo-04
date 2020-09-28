#No exercício da última semana, de desenvolver um sistema para verificar se a
#pessoa está apta para doação de sangue, você criou todo o sistema sem utilizar
#funções. Nessa nova versão mantenha os recursos e verificações que foram
#propostas, porém, separe em funções as validações e recursos. Exemplo: função
#para fazer a validação se a pessoa está apta: def validaRequisitos(): onde dentro do
#escopo da função, você deve colocar o processo de validação e retornar true ou
#false para mostrar ao usuário se ele está apto ou não. 


#Fiquei com dificuldade para fazer esse exercício, professora. Tentei adaptar ao meu exercício anterior.
S=0
usuario=0
doadorIdade = []
doadorPeso = []
doadorSono = []

def cadastro():
    doadorIdade.append(input("Informe sua idade"))
    doadorPeso.append(input("informe seu peso"))
    doadorSono.append(input("informe quantas horas de sono você dormiu na última noite"))

#Verificando se o doador se adequa na idade
if (doadorIdade>16) and (doadorIdade<69):
    print("Você possui idade para doar sangue!")
else:
    print("Ah não! Você não possui idade para doar")

#Verificando se o doador se adequa no peso
if doadorPeso>50:
    print("Você está no peso ideal para doar sangue!")
else:
    print("Você não se adequa ao peso que requesitamos")

#Verificando se o doador se adequa nas horas de sono
if doadorSono>6:
    print("Sua noite de sono foi bela, você já pode doar!")
else:
    print("Você não pode doar. Volte para casa e descanse")

#Verificando se o doador deseja se cadastrar
cadastro = float(input("Você deseja se cadastrar conosco (S/N)?"))
if cadastro == S:
    usuario=(input("Informe seu nome completo:"))




