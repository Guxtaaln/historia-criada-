import random

# Função que cria o início da história 

def criar_início():
    início = ["Em um bairro não tão conhecido", "Por volta de um ano."]
    return random.choice(início)

# Função que cria o centro da história 
def criar_centro():
    centro =  ["iniciava um curso" , "jovens se uniam em busca de aprendizado" , "entravam na jornada de trabalho."]
    return  random.choice(centro)

# Função pricipal que cria o final da história 
def criar_final():
    finais =  ["belas amizades se formavam" , "uma jovem acaba se distanciando por mudar de escola" , "assim se inicia o uma nova jornada em suas vidas."]

return random.choice(final)

# Função principal que cria toda a história 
def criar_historia():
    início = criar_inicio()
    centro = criar_centro()
    final = criar_final()

    historia = f"{inicio} {centro} {final}"
    return historia

# Exibe a história gerada 
if  __name_ == "__main__":
    print(criar_historia())


