#####################################################
# Tarefas não gráficas
# Tarefa 9.1 - Login
# Aluno: Everton Pereira Militão
# Matrícula:2320462
#####################################################
# Usar somente python com a tela interativa.
# Não é para usar o Pygame e nem o Turtle.
#####################################################
from colorama import init, Fore, Back, Style
init()

def valida_cpf(cpf):
  #Remove os caracteres não numéricos
  cpf = ''.join(filter(str.isdigit,cpf))

  #Verifica se o cpf tem 11 digitos 
  if len(cpf) != 11:
    return False

  #Verfica se todos os digitos são iguais
  if cpf == cpf[0] * 11:
    return False

  #Calcula e verifica o primeiro digito verificador
  total = 0
  for i in range(9):
    total += int(cpf[i]) * (10 - i)
  resto = total % 11

  digito1 = 0 if resto < 2 else 11 - resto 

  if digito1 != int(cpf[9]):
    return False

  #Calcula e verifica o segundo digito verificador
  total = 0
  for i in range(10):
    total += int(cpf[i]) * (11 - i)
  resto = total % 11

  digito2 = 0 if resto < 2 else 11 - resto 

  if digito2 != int(cpf[10]):
    return False
    
  #Se o CPF for Válido
  return True

#Bloco Principal:
cpf_exemplo = str(input("Digite o cpf:"))
if valida_cpf(cpf_exemplo):
  print(Fore.BLUE + "O CPF %s é válido" %cpf_exemplo)

else:
  print(Fore.RED + "O CPF %s é inválido" %cpf_exemplo)

