# Di dalam bahasa pemrograman Python pengulangan dibagi menjadi 3 bagian, yaitu :
# While Loop
# For Loop
# Nested Loop

#while Loop

mulai = 0
while ( mulai < 10):
  mulai += 1 # menambahkan nilai 1 setiap perulangan yang dilakukan
  print(mulai)

print(" Perulangan selesai\n")

#for
angka = [1, 2, 3, 4, 5]
for num in angka:
  print(num)

print(" Perulangan selesai\n")


for i in range(1, 9):
  print(i)
print("Perulangan selesai\n")


buah = ["semangka", "apel", "jeruk"]
for makanan in buah:
    print ("buah", makanan)


# nested loop
i = 2
while(i < 50):
  j = 2
  while(j <= (i/j)):
      if not(i%j): 
        break
      j = j + 1
  if (j > i/j): 
    print(i, "bilangan prima")
  i = i + 1

print("selesai\n")

rows = 5
for i in range(1, rows + 1):
  for j in range(1, i + 1):
      print("*", end=" ")
  print('')