def case(text, res):
    for i in range(len(text)):
        if text[i].isupper():
            res[i] = res[i].upper()
    return(''.join(res))


def alphabet(language):
    if language == "р":
        return ord("а"), ord("я") + 1
    elif language == "а":
        return ord("a"), ord("z") + 1


def encrypt(language, shift, text):
    left, right = alphabet(language)
    res = []
    for el in text.lower():
        if el.isalpha() == False:
            res.append(el)
        elif ord(el) + shift >= right:
            res.append(chr(left + (shift - (right - ord(el)))))
        else:
            res.append(chr(ord(el) + shift))
    return(case(text, res))

def decrypt(language, shift, text):
    left, right = alphabet(language)
    res = []
    for el in text.lower():
        if el.isalpha() == False:
            res.append(el)
        elif ord(el) - shift < left:
            res.append(chr(right - (shift - (ord(el) - left))))
        else:
            res.append(chr((ord(el) - shift)))
    return(case(text, res))


mode = input("Шифруем или дешифруем? (ш/д) ")
language = input("Русский или английский? (р/а) ")
shift = int(input("Введите шаг сдвига: "))
if mode == "ш":
    text = input("Введите текст для шифрования: ")
else:
    text = input("Введите текст для дешифрования: ")

if mode == "ш":
    print(encrypt(language, shift, text))
else:
    print(decrypt(language, shift, text))
