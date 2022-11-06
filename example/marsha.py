

n = int(input("masukkan jumlah data: "))
list_data=[int(input("masukkan data: %d")) for _ in range(n)] #'_' abis for wajib
sum = 0 
maxNum = list_data[0]
minNum = list_data[0]
for i in list_data:
  if maxNum < i: 
      maxNum = i
  if minNum > i:
    minNum = i


print('nilai terbesar pada list: ', maxNum)
print('nilai terkecil pada list: ', minNum)