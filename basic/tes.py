array = [1,2,3,4,5]

search = int(input("cari : "))
for idx, val in enumerate(array):
  print(idx)
  if search == val:
    print("Data ditemukan")
    break  
else:
  print("Nothing")