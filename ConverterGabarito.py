# ===========2019===========

def converter_lista(lista: list) -> str:
    caracteres_para_remover = "[] \',"
    return ''.join(x for x in lista if x not in caracteres_para_remover)
    # Adiciona na str apenas os elementos que não estão na str caracteres_para_remover
    
    
def converter_azul(codigo: int, respostas: str) -> str:
    azul = [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150,
            151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165,
            166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180]
    amarela = [139, 140, 141, 163, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154,
               155, 156, 157, 158, 159, 160, 161, 162, 164, 165, 166, 167, 168, 169, 170,
               171, 172, 173, 174, 136, 137, 138, 176, 177, 178, 179, 180, 175, 142, 143]
    cinza = [151, 152, 153, 177, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146,
             147, 148, 149, 150, 173, 174, 175, 176, 154, 155, 156, 157, 158, 159, 160,
             161, 162, 163, 164, 165, 166, 167, 178, 179, 170, 171, 172, 180, 168, 169]
    rosa = [142, 143, 144, 167, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158,
            159, 160, 161, 162, 163, 164, 165, 166, 170, 171, 172, 173, 174, 175, 176,
            177, 178, 179, 180, 145, 146, 147, 168, 169, 138, 139, 140, 141, 136, 137]
    # Listas com as questões conrrespondentes para a conversão
    if codigo == 515:
        lista_base = azul
    elif codigo == 516:
        lista_base = amarela
    elif codigo == 517:
        lista_base = rosa
    elif codigo == 518:
        lista_base = cinza
    respostas = list(respostas)
    respostas_azul = respostas.copy()
    for i in range(0, 45):
        posicao_no_azul = lista_base[i]-135-1
        # Para calcular usa a lista com as questões respectivas comparando com a prova azul
        # Como as questões comecam na 136, se subtrai 135 e também se subtrai 1 porque o índice
        # comeca com 0
        respostas_azul[i] = respostas[posicao_no_azul]
        # O valor azul na posicao i recebe o valor amarela na posição correspondente
    return converter_lista(respostas_azul)


if __name__ == '__main__':
    num = int(input("Num: "))
    gab = input("Gabarito: ")
    print(converter_azul(num, gab))
    # Código usado só para testes
