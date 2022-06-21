def searchMax(listNum):
  greatest_number = listNum[0]

  if len(listNum) > 1:
    next_greatest_number = searchMax(listNum[1:])
    if next_greatest_number > greatest_number:
      greatest_number = next_greatest_number
  return greatest_number

def searchMin(listNum):
  smallest_number = listNum[0]

  if len(listNum) > 1:
    next_smallest_number = searchMax(listNum[1:])
    if next_smallest_number < smallest_number:
      smallest_number = next_smallest_number
  return smallest_number

numberList = [21, 39 , 48, 50]
print(numberList)
print('Nilai terbesar: ', searchMax(numberList))
print('Nilai Terkecil: ', searchMin(numberList))
