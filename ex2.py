def calcula_bonus(nota_original, nota_segunda_chance):
    bonus = 0
    if nota_segunda_chance == 10:
        bonus = 2
    return min(nota_original + bonus, 10)

# Leitura do número de alunos
n = int(input())

notas_originais = []
notas_segunda_chance = []

# Leitura das notas originais
for i in range(n):
    nota_original = float(input())
    notas_originais.append(nota_original)

# Leitura das notas da "Segunda Chance"
for i in range(n):
    nota_segunda_chance = float(input())
    notas_segunda_chance.append(nota_segunda_chance)

# Contador de alunos com notas alteradas
alunos_com_notas_alteradas = 0

# Cálculo das notas finais
for i in range(n):
    nota_original = notas_originais[i]
    nota_segunda_chance = notas_segunda_chance[i]
    nota_final = calcula_bonus(nota_original, nota_segunda_chance)

    if nota_final > nota_original:
        alunos_com_notas_alteradas += 1

# Exibição da quantidade de alunos com notas alteradas
print(f'NOTAS ALTERADAS: {alunos_com_notas_alteradas}')

# Exibição das notas originais e finais
for i in range(n):
    nota_original = notas_originais[i]
    nota_segunda_chance = notas_segunda_chance[i]
    nota_final = calcula_bonus(nota_original, nota_segunda_chance)
    print(f"{'-' if nota_final == nota_original else '*'}({i+1:03d}) original: {nota_original:05.2f} | final: {nota_final:05.2f}")
