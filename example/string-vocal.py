sentence = input('Masukkan Kalimat atau kata: ').lower()
dictionary_string_vocal = { 'a': 0, 'i': 0, 'u': 0, 'e': 0, 'o': 0 }

for item_vocal in dictionary_string_vocal.keys():
  dictionary_string_vocal[item_vocal] = sentence.count(item_vocal)

total_string_vocal = sum(dictionary_string_vocal.values())

print(f'Panjang Kalimat atau kata: {len(sentence)} huruf')
print(f'Total Huruf Vokal : {total_string_vocal}')

print(f"""\
  a -> {dictionary_string_vocal['a']}
  i -> {dictionary_string_vocal['i']}
  u -> {dictionary_string_vocal['u']}
  e -> {dictionary_string_vocal['e']}
  o -> {dictionary_string_vocal['o']}\
""")