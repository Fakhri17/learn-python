def convertBin(num):
  if num < 0:
    return "Number must be integer positif"
  elif num == 0:
    return '0'
  else:
    return convertBin(num//2) + str(num%2)

decimal_number = 10
print(decimal_number)
print(convertBin(decimal_number))

