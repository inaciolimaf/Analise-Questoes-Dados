import FuncoesDados

# Segunda parte para converter as respostas para equivalerem as da prova Azul

microdados = FuncoesDados.MicrodadosENEM("MicrodadosFiltrados.csv")

print("Iniciando o calculo:")
microdados.converter_gabarito()
print("Processo concluído. O resultado é:")
print(microdados.microdados)

microdados.exportar_dados("MicrodadosFiltradosConvertido.csv")
