def maior_iterativo(lista):
    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero

    return maior


def maior_recursivo(lista):
    if len(lista) == 1:
        return lista[0]

    maior_resto = maior_recursivo(lista[1:])

    if lista[0] > maior_resto:
        return lista[0]
    else:
        return maior_resto


def valida_cpf(cpf):
    # Remove pontos e traços
    cpf = cpf.replace(".", "").replace("-", "")


    if len(cpf) != 11:
        return False


    if cpf == cpf[0] * 11:
        return False


    soma = 0

    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    resto = (soma * 10) % 11

    if resto == 10:
        resto = 0

    if resto != int(cpf[9]):
        return False


    soma = 0

    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    resto = (soma * 10) % 11

    if resto == 10:
        resto = 0

    if resto != int(cpf[10]):
        return False

    return True


if __name__ == "__main__":

    lista_teste = [3, 9, 2, 7]

    print("Maior iterativo:", maior_iterativo(lista_teste))
    print("Maior recursivo:", maior_recursivo(lista_teste))

    cpf_teste = "529.982.247-25"

    if valida_cpf(cpf_teste):
        print("CPF válido")
    else:
        print("CPF inválido")
