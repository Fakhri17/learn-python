setence = input("Masukkan Kalimat atau kata: ").lower()
replaceString = 'i'

for itemString in 'aiueo':
  setence = setence.replace(itemString, replaceString)

print(setence)