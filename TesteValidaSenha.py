def validaSenha(senha):
    if len(senha) < 8:
        return False

    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabetoM = alfabeto.upper()
    numeros = "0123456789"

    for char in senha:
        if char in alfabeto or char in alfabetoM or char in numeros:
            continue
        else:
            return False

    return True

# Bloco Principal:
senha = input("Digite sua senha: ")

if validaSenha(senha):
    print("Senha Válida!")
else:
    print("Senha inválida!")
