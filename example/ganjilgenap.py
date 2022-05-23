# basic usage

# number1 = int(input('Masukkan Angka: '))
# if number1 % 2 != 0 :
#   print(f'{number1} merupakan bilangan ganjil')
# else:
#   print(f'{number1} merupakan bilangan genap')

#  from range
# print('Massukan nilai awal dan akhir')
# ganjil = []
# genap = [] 
# nilai_awal = int(input('Masukkan Nilai Awal: '))
# nilai_akhir = int(input('Masukkan Nilai Akhir: '))

# for number_range in range(nilai_awal, nilai_akhir + 1):
#   if number_range % 2 != 0:
#     ganjil.append(number_range)
#   else:
#     genap.append(number_range)

# print(f'Bilangan Ganjil = {ganjil}')
# print(f'Bilangan Genap = {genap}')


# from range with selected condition
print('Masukkan nilai awal dan nilai akhir')

nilai_awal = int(input('Masukkan Nilai Awal : '))
nilai_akhir = int(input('Masukkan Nilai Akhir : '))

print("""\nTampilkan bilangan
 1. Ganjil
 2. Genap""")

pilihan = int(input('Pilihan: '))

if pilihan not in [1, 2]:
  print('pilihan tidak tersedia')
else:
  for number_range in range(nilai_awal, nilai_akhir + 1):
    if pilihan == 1 and number_range % 2 == 1:
      print(number_range, end=' ')
    elif pilihan == 2 and number_range % 2 == 0:
      print(number_range, end=' ')