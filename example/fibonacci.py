# credits: https://jagongoding.com/python/latihan-logika/fibonacci-non-rekursif/

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