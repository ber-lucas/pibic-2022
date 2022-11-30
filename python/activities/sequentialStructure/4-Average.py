#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
note = list(range(0,4))

for x in range(4): 
  note[x] = int(input('Nota do bimestre: '))

average = (sum(note)) / len(note)
print('A média das notas é:', average)