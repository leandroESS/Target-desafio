vet = [22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612, 0.0, 42889.2258, 42889.2258, 11191.4722, 0.0, 0.0,
3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614, 0.0, 0.0, 35240.1826, 43829.1667, 18235.6852, 18235.6852,
13327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 13220.495, 8414.61]

# O menor valor de faturamento ocorrido em um dia do mês;
print(max(vet))

# O maior valor de faturamento ocorrido em um dia do mês;
print(min(vet))

# Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
media = sum(vet) / len(vet)

cont = 0
for i in vet:
    if i > media:
        cont += 1

print(cont)