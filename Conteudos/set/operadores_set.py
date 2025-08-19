# " | "  - Unir dois sets;

# " & " - Itens que estão presentes em ambos os sets;

# " - " - Itens presentes apenas no set da esquerda;

# " ^ " - Itens que não estão presentes em ambos.


s1 = {1, 2, 3, 4}
s2 = {1, 2, 35, 97, 90}


# Vai unir os dois set's
s3 = s1 | s2
print(f'União: {s3};')

print()

# Separa só os itens que tem em ambos os set´s
s3 = s1 & s2

print(f'Intersecção: {s3};')

print()

# São os itens que estão apenas nos set´s da esquerda ( primeiro set )
s3 = s1 - s2

print(f'Diferença: {s3};')

print()

# São que os não tem em ambos os set´s
s3 = s1 ^ s2

print(f'Diferença simétrica: {s3};')

print()
