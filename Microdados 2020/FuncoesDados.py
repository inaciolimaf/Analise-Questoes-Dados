import pandas as pd
from tqdm import tqdm
from ConverterGabarito import *

# Todo essa parte é só para funcionar a orientação à objeto
# Ela não é obrigatória para chegar no resultado
# O jeito mais fácil seria usar o Jupyter e sem Orientação à objeto
# Fiz usando isso para poder aprender


class MicrodadosENEM:
    def __init__(self, nome=None, colunas=None, ler_microdados=True, microdados=None):
        if ler_microdados:
            print("Importando...")
            self.microdados = pd.read_csv(nome, sep=';', encoding='latin-1', usecols=colunas)
            # Lê os microdados
            print("Importado")
        else:
            self.microdados = microdados
        # Divide em duas partes porque em uma parte do código será preciso criar uma objeto
        # sem fazer a leitura de um arquivo
        self.gabaritoConvertido = []
        # Cria uma lista para ser preenchidda em outra função com as respostas convertidas
        # para a prova azul e depois adicionada nos microdados
        self.materia = "MT"
        # Matéria que será calculada

    def localiza_valor_nos_microdados(self, num):
        return self.microdados.loc[self.microdados[f"CO_PROVA_{self.materia}"] == num]

    @classmethod
    def filtrar_dados(cls, microdados, lista_de_usados):
        novos_microdados = None
        for i, num in enumerate(lista_de_usados):
            if i == 0:
                # Se for a primeira vez no laço é preciso criar um novo dataframe
                micro_filtrados = microdados.localiza_valor_nos_microdados(num)
                novos_microdados = micro_filtrados
                # Cria o dataframe "novos_microdados"
            else:
                # Senão for a primeira vez é preciso juntar(merge) os dois dataframes
                micro_filtrados = microdados.localiza_valor_nos_microdados(num)
                novos_microdados = pd.merge(novos_microdados, micro_filtrados, how='outer')
                # Juntando os dataframes
        return cls(ler_microdados=False, microdados=novos_microdados)
        # Retorna um objeto com os novos microdados

    def exportar_dados(self, nome):
        print("Exportando...")
        self.microdados.to_csv(nome, index=False, sep=';', encoding='latin-1')
        print("Processo concluído")

    def converter_gabarito(self):
        quantidade_de_linhas = self.microdados.loc[:, f"CO_PROVA_{self.materia}"].count()
        for i in tqdm(range(0, quantidade_de_linhas)):
            # O tqdm é para criar a barra de progresso
            self.gabaritoConvertido.append(converter_azul(self.microdados.iloc[i][f"CO_PROVA_{self.materia}"],
                                                         self.microdados.iloc[i][f"TX_RESPOSTAS_{self.materia}"]))
            # Para cada linha converte o gabarito usando a função e adiciona em uma lista
        self.microdados[f"TX_RESPOSTAS_{self.materia}"] = self.gabaritoConvertido
        # Coloca a lista nos microdados
        self.microdados[f"TX_GABARITO_{self.materia}"] = "EEEADBEBACABCDBABECECACDCBDCCEDCDABEDECDDDBAA"
        # Atualiza também o gabarito

    @staticmethod
    def _formatar_porcentagem(num):
        return f"{(num*100):.1f}%"
        # Função que retorna um string que representa a porcetagem

    @staticmethod
    def _criar_dataframe(lista_com_todas_questoes):
        resultado_microdados = pd.DataFrame(lista_com_todas_questoes, columns=["QUESTAO",
                                                                               "A", "B", "C", "D",
                                                                               "E", "ANULADA", "ACERTOS"])
        # Cria o DataFrame basedo na lista com os resultados
        print("Exportando...")
        resultado_microdados.to_excel("ResultadoMicrodados.xlsx", index=False)
        print("Processo concluído")
        # Exporta os resultados para um arquivo .xlsx
    
    def exportar_resultado(self):
        lista_com_todas_questoes = []
        gabarito_completo = "EEEADBEBACABCDBABECECACDCBDCCEDCDABEDECDDDBAA"
        quantidade_de_linhas = self.microdados.loc[:, f"CO_PROVA_{self.materia}"].count()
        for questao in tqdm(range(0, 45)):
            cont_total = 0
            cont_a = 0
            cont_b = 0
            cont_c = 0
            cont_d = 0 
            cont_e = 0
            cont_anulada = 0
            # Zera todos os valores que seram calculados
            for i in range(0, quantidade_de_linhas):
                # Faz a análise linha por linha
                alternativa = self.microdados.loc[i, f"TX_RESPOSTAS_{self.materia}"][questao]
                # Pega cada alternativa marcada na questão para cada candidato
                if alternativa == 'A':
                    cont_a += 1
                elif alternativa == 'B':
                    cont_b += 1
                elif alternativa == 'C':
                    cont_c += 1
                elif alternativa == 'D':
                    cont_d += 1
                elif alternativa == 'E':
                    cont_e += 1
                else:
                    cont_anulada += 1
                cont_total += 1
                # Faz os cálculos de cada variável
            gabarito_unico = gabarito_completo[questao]
            if gabarito_unico == 'A':
                acertos = cont_a/cont_total
            elif gabarito_unico == 'B':
                acertos = cont_b/cont_total
            elif gabarito_unico == 'C':
                acertos = cont_c/cont_total
            elif gabarito_unico == 'D':
                acertos = cont_d/cont_total
            elif gabarito_unico == 'E':
                acertos = cont_e/cont_total
            else:
                acertos = 1
            # Calcula a quantidade de acertos para cada questao
            lista_com_uma_questao = [questao+136, self._formatar_porcentagem(cont_a/cont_total),
                                     self._formatar_porcentagem(cont_b/cont_total),
                                     self._formatar_porcentagem(cont_c/cont_total),
                                     self._formatar_porcentagem(cont_d/cont_total),
                                     self._formatar_porcentagem(cont_e/cont_total),
                                     self._formatar_porcentagem(cont_anulada/cont_total),
                                     self._formatar_porcentagem(acertos)]
            lista_com_todas_questoes.append(lista_com_uma_questao)
            # Junta o resultado em uma lista
        self._criar_dataframe(lista_com_todas_questoes)
