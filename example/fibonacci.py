# Bilangan fibonacci selalu diawali oleh 2 angka, yaitu 0 dan 1.
# Ke-3 adalah hasil dari 0 + 1 = 1
# Ke-4 adalah hasil dari 1 + 1 = 2
# Ke-5 adalah hasil dari 2 + 1 = 3
# Ke-6 adalah hasil dari 3 + 2 = 5
# Ke-7 adalah hasil dari 5 + 3 = 8 dst

panjangBilangan = int(input(" Masukkan deret bilangan yang di inginkan = "))
fibo = [0, 1]

for i in range(2, panjangBilangan):
  bil1 = fibo[i - 2]
  bil2 = fibo[i - 1]
  total = bil1 + bil2
  print(f'deret ke {(i + 1)} adalah {bil1} + {bil2} = {total}')
  fibo.append(total)

print(fibo)
  # index1 = i - 2
  # index2 = i - 1
  # print(f'deret ke {(i + 1)} adalah index-{index1} + index-{index2}')