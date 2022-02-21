def converter_lista(lista : list) -> str:
    caracteresParaRemover = "[] \',"
    return ''.join(x for x in lista if x not in caracteresParaRemover)
    # Adiciona na str apenas os elementos que não estão na str caracteresParaRemover
    
def converter_azul(codigo: int, respostas: str) -> str:
    azul    = [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150,
            151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165,
            166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180]
    amarela = [148, 149, 150, 151, 152, 153, 163, 164, 165, 138, 139, 140, 155, 156, 157,
            158, 145, 146, 147, 166, 167, 141, 142, 143, 144, 168, 169, 170, 171, 172,
            173, 174, 175, 176, 177, 178, 179, 180, 154, 136, 137, 159, 160, 161, 162]
    cinza   = [146, 147, 168, 169, 170, 171, 161, 162, 163, 173, 174, 175, 136, 137, 138,
            139, 141, 142, 143, 176, 177, 156, 157, 158, 159, 148, 149, 150, 151, 178,
            179, 180, 164, 165, 166, 167, 144, 145, 172, 140, 160, 152, 153, 154, 155]
    rosa    = [179, 180, 158, 159, 160, 161, 172, 173, 174, 163, 164, 165, 175, 176, 177, 
            178, 169, 170, 171, 147, 148, 143, 144, 145, 146, 154, 155, 156, 157, 140,
            141, 142, 150, 151, 152, 153, 166, 167, 149, 162, 168, 136, 137, 138, 139]
    if codigo == 587:
        listaBase = azul
    elif codigo == 588:
        listaBase = amarela
    elif codigo == 590:
        listaBase = cinza
    elif codigo == 589:
        listaBase = rosa
    respostas = list(respostas)
    respostas_azul = respostas.copy()
    for i in range(0, 45):
        posicao_no_azul = listaBase[i]-135-1
        # Para calcular usa a lista com as questões respectivas comparando com a prova azul
        # Como as questões comecam na 136, se subtrai 135 e também se subtrai 1 porque o índice
        # comeca com 0
        respostas_azul[i] = respostas[posicao_no_azul]
        # O valor azul na posicao i recebe o valor amarela na posição correspondente
    return converter_lista(respostas_azul)