import statistics 

def calcular_estatisticas(notas):
    print("--- Estatísticas das Notas ---")
    print(f"Média: {statistics.mean(notas):.2f}")
    print(f"Moda: {statistics.mode(notas) if len(set(notas)) < len(notas) else 'Sem moda'}")
    print(f"Desvio Padrão: {statistics.stdev(notas):.2f}" if len(notas) > 1 else "DP: Dados insuficientes")
    print(f"Maior nota: {max(notas)}")
    print(f"Menor nota: {min(notas)}")

notas_alunos = [8.5, 7.0, 9.5, 7.0, 6.5, 10.0, 8, 8.5]
calcular_estatisticas(notas_alunos)

