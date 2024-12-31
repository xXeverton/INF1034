#####################################################
# Tarefas não gráficas
# Tarefa 9.2 - Senha
# Aluno:Everton Pereira Militão
#####################################################
# Usar somente python com a tela interativa.
# Não é para usar o Pygame e nem o Turtle.
#####################################################
#módulo
from getpass import getpass  #  Só para ocultar a senha ao inseri-la
from colorama import init, Fore, Back, Style

init()


#Função
def verificaSenha(senha):
    # Verifica o tamanho da senha:
    if len(senha) < 8:
        return False

    #Caracteres que devem estar na senha inserida pelo usuário
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabetoM = alfabeto.upper()
    numeros = "0123456789"

    #Verifica para cada carcter da senha se ele está no alfabeto ou números.
    for caracter in senha:
        if caracter in alfabeto or caracter in alfabetoM or caracter in numeros:
            continue
        #Caso o caracter não esteja no alfabeto, números ou espaço, retorna "False"
        else:
            return False

    return True


#Bloco principal:
print("Cadastre sua senha com os seguintes critérios:\n"
      "- Deve ter no mínimo 8 caracteres\n"
      "- Deve ter ao menos uma letra MAIÚSCULA\n"
      "- Deve ter ao menos uma letra minuscula\n"
      "- Deve ter ao menos um número\n")

usuario = input("Digite seu nome de usuário:")
#Oculta a senha ao inserir "getpass"
senha = getpass("Digite sua senha:")
if verificaSenha(senha):
    print(Fore.BLUE + "Senha cadastrada com sucesso!")

else:
    print(Fore.RED + "Senha inválida!")
