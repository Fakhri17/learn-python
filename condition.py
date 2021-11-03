# Kondisi If
# Pengambilan keputusan (kondisi if) digunakan untuk mengantisipasi kondisi yang terjadi saat jalanya program dan menentukan tindakan apa yang akan diambil sesuai dengan kondisi.

# Pada python ada beberapa statement/kondisi diantaranya adalah if, else dan elif Kondisi if digunakan untuk mengeksekusi kode jika kondisi bernilai benar True.

nilai = 9 # ubah value variabel yg di inginkan

#jika kondisi benar/TRUE maka program akan mengeksekusi perintah dibawahnya
if (nilai > 8):
  print(" akan di eksekusi ") # eksekusi

if ( nilai > 11):
  print(" Tidak di eksekusi ") # tidak 


#else conditions
if(nilai > 9):
  print("Selamat kamu lulus dari ujian")
else:
  print("Kamu tidak lulus ujian")

#elif condition
if(nilai > 9):
  print("Selamat kamu lulus dari ujian")
elif(nilai == 9):
  print(" Nilai kamu masuk KKM, boleh ikut remidi atau tidak")
else:
  print("Kamu tidak lulus ujian")