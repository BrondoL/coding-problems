# Hitung Frekuensi Karakter

sentence = input()
result = {}

for letter in sentence:
    if not letter.isalpha():
        continue
    if letter in result:
        result[letter] += 1
    else:
        result[letter] = 1

for key, value in sorted(result.items()):
    print(key, value)