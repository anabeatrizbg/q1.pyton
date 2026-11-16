notas = []

for i in range(6):

 nota = float(input("Digite sua nota: "))

while nota < 0 or nota > 10:
      print("Nota invalida! Digite novamente.")
      nota = float(input("Digite sua nota: "))

notas.append(nota)

print(notas)

soma = 0
for nota in notas:
    soma = soma + nota
    media = soma / len(notas)

print("Media da turma: ", round(media, 2))
