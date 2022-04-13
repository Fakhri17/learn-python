# Bilangan prima adalah bilangan lebih dari 1 yang hanya memiliki 2 faktor (pembagi) saja: yaitu 1 dan dirinya
# sendiri. Artinya, sebuah bilangan prima tidak bisa dibagi dengan pembagi apa pun kecuali dengan angka 1 dan
# dirinya sendiri

# Contoh bilangan prima adalah angka 2: ia tidak memiliki pembagi apa pun selain 1 dan 2.
# Contoh lain adalah bilangan 3. Bilangan 3 tidak bisa dibagi kecuali dengan angka 1 dan 3.
# Dan contoh yang bukan bilangan prima adalah 4: karena ia memiliki pembagi lain selain angka 1 dan dirinya sendiri, yaitu angka 2.

def is_prima (num):
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

print(is_prima(5))
print(is_prima(2))
print(is_prima(4))
print(is_prima(11))

def cari_bilangan_prima (awal, akhir):
  list_bilangan_prima = []

  for x in range(awal, akhir + 1):
    if is_prima(x):
      list_bilangan_prima.append(x)

  return list_bilangan_prima

bilAwal = int(input('Masukkan angka awal: '))
bilAkhir = int(input('Masukkan angka akhir: '))
print('Berikut hasil bilangan primanya')
print(cari_bilangan_prima(bilAwal, bilAkhir))