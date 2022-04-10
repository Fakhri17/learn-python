
kendaraan = input("Kendaraaan : ")
if kendaraan == "Motor" or  kendaraan == "motor":
  print("Kendaraan Motor")
  lama_waktu = int(input(" Lama waktu : "))
  totalBiaya = 0
  if lama_waktu == 1 :
    totalBiaya = 1000
  elif lama_waktu == 2 or  lama_waktu == 3:
    totalBiaya = 2000
  elif lama_waktu > 3 :
    totalBiaya = 2000 + (lama_waktu-3) * 500
  else:
    print("NULL")
  print(totalBiaya)

elif kendaraan == "Mobil" or kendaraan == "mobil":
  print("Kendaraan Mobil")
  lama_waktu = int(input(" Lama waktu : "))
  totalBiaya = 0
  if lama_waktu == 1 :
    totalBiaya = 2000
  elif lama_waktu == 2 or  lama_waktu == 3:
    totalBiaya = 3000
  elif lama_waktu > 3 :
    totalBiaya = 3000 + (lama_waktu-3) * 1000
  else:
    print("NULL")
  print(totalBiaya)

elif kendaraan == "Truck" or kendaraan =="truck":
  print("Kendaraan truck")
  lama_waktu = int(input(" Lama waktu : "))
  totalBiaya = 0
  if lama_waktu == 1 :
    totalBiaya = 3000
  elif lama_waktu == 2 or  lama_waktu == 3:
    totalBiaya = 4000
  elif lama_waktu > 3 :
    totalBiaya = 4000 + (lama_waktu-3) * 2000
  else:
    print("NULL")
  print(totalBiaya)

else:
  print("Kendaraan Tidak terdaftar")

