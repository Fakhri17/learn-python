
def mean(dataList):
  return sum(dataList) / len(dataList)

def median(dataList):
  dataList.sort()
  lenghtList = len(dataList)
  mid_data = lenghtList // 2
  
  return dataList[mid_data] if lenghtList % 2 == 1 else (dataList[mid_data - 1] + dataList[mid_data]) / 2

def modus(dataList):
  peta_kemunculan = {}

  # perulangan satu-persatu tiap bilangan
  for item_number in dataList:
    # periksa apakah sudah pernah muncul atau belum
    if item_number in peta_kemunculan:
      peta_kemunculan[item_number] += 1
    else:
      peta_kemunculan[item_number] = 1

  # cari kemunculan terbanyak
  bilangan_terbesar = dataList[0] # ambil angka pertama sebagai yg terbanyak
  for bilangan in peta_kemunculan.keys():
    jumlah = peta_kemunculan[bilangan]

    if jumlah > peta_kemunculan[bilangan_terbesar]:
      bilangan_terbesar = bilangan

  return bilangan_terbesar
  
inputListNumber = input('Masukkan urutan angka (ex: 1 2 3 4 5 6) : ')
# dataNumber = list(map(int,str(inputListNumber)))
dataNumber = []
for item_number in inputListNumber.split(' '):
    dataNumber.append(int(item_number))

mean = mean(dataNumber)
median = median(dataNumber)
modus = modus(dataNumber)

print(dataNumber)
print(f'Mean = {mean}')
print(f'Median = {median}')
print(f'Modus = {modus}')