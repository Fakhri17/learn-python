# Bilangan fibonacci selalu diawali oleh 2 angka, yaitu 0 dan 1.
# Ke-3 adalah hasil dari 0 + 1 = 1
# Ke-4 adalah hasil dari 1 + 1 = 2
# Ke-5 adalah hasil dari 2 + 1 = 3
# Ke-6 adalah hasil dari 3 + 2 = 5
# Ke-7 adalah hasil dari 5 + 3 = 8 dst

def fibonacci(data):
  if data < 1:
    return [data]

  listSebelumN = fibonacci(data - 1)
  angka1 = listSebelumN[-2] if len(listSebelumN) > 2 else 0
  angka2 = listSebelumN[-1] if len(listSebelumN) > 2 else 1

  print(f'{angka1} + {angka2} = {angka1 + angka2}')
  return listSebelumN + [angka1 + angka2]

panjang = int(input('Masukkan panjang deret: '))
print(fibonacci(panjang - 1))