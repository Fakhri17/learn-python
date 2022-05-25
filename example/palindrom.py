dataMonth = {
  'Januari': '01', 'Februari': '02', 'Maret': '03', 'April': '04', 'Mei': '05', 'Juni': '06',
  'Juli': '07', 'Agustus': '08', 'September': '09', 'Oktober': '10', 'November': '11', 'Desember': '12',
}

def isPalindrome(str):
  for i in range(0, int(len(str)/2)):
    if str[i] != str[len(str)-i-1]:
      return False
  return True

dateDays = input("Tanggal: ")
dateMonth = input("Bulan (Nama bulan misal Januari): ")
dateYear = input("Tahun: ")

for key in dataMonth:
  if key == dateMonth.capitalize():
    idMonth = dataMonth[key]

allDate = dateDays + idMonth + dateYear
if isPalindrome(allDate):
  print('This is Palindrome')
else:
  print('Not Palindrome')

