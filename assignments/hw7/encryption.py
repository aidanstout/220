def encode():
    output = ""
    for letter in message:
        number = ord(letter)
        code = chr(number + key)
        output = output + code
    print(output)


def encode_better():
    output = ""
    for i in range(len(text)):
        character = ord(text[i]) - 65
        key_character = ord(key[i % len(key)]) - 65
        code = character + key_character
        code = code % 58
        code = code + 65
        output = output + chr(code)
    print(output)