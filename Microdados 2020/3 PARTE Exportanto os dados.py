import FuncoesDados

# Terceira parte para exportar o resultado

microdados = FuncoesDados.MicrodadosENEM("MicrodadosFiltradosConvertido.csv")
microdados.exportar_resultado()

print("Concluído.")
