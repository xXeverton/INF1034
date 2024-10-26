
def valida_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Calcula e verifica o primeiro dígito verificador
    total = 0
    for i in range(9):
        total += int(cpf[i]) * (10 - i)
    resto = total % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto
    if digito1 != int(cpf[9]):
        return False

    # Calcula e verifica o segundo dígito verificador
    total = 0
    for i in range(10):
        total += int(cpf[i]) * (11 - i)
    resto = total % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto
    if digito2 != int(cpf[10]):
        return False

    # CPF é válido
    return True

# Exemplo de uso
cpf_exemplo = str(input("Digite Cpf:"))
if valida_cpf(cpf_exemplo):
    print(f"O CPF {cpf_exemplo} é válido.")
else:
    print(f"O CPF {cpf_exemplo} é inválido.")
