def balik_string(teks):
    stack = []
    for char in teks:
        stack.append(char)

    hasil = ''
    while stack:

        hasil += stack.pop()
    return hasil

print(balik_string('haiii'))
print(balik_string('stepnotonpets'))
print(balik_string('haiii'))