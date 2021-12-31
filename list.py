year = [2018, 2019, 2020, 2021, 2022]
kelas = ["X", "XI", "XII", "FREE", "SEM 1"]

print(year[1])
print(kelas[0:3])


myDict = dict(zip(year, kelas))

print(myDict)

for key, value in myDict.items():
  print("Tahun", key, "Kelas", value)