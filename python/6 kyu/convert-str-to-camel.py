# Доработайте метод/функцию таким образом, чтобы он преобразовывал слова,
# разделенные тире/андерскором, в верблюжий регистр.
# Первое слово в выходных данных должно быть написано с заглавной буквы только в том случае,
# если исходное слово было написано с заглавной буквы
# (так называемый верхний регистр верблюда, также часто называемый регистром Паскаля).
# Последующие слова всегда должны быть прописными.

# Примеры
# "the-stealth-warrior" преобразуется в "theStealthWarrior"

# "The_Stealth_Warrior" преобразуется в "TheStealthWarrior"

# "The_Stealth-Warrior" преобразуется в "TheStealthWarrior"

text = "the-stealth_warrior"


def to_camel_case(text):
    text = text.replace('_', '-')
    arr = text.split('-')
    for i in range(1, len(arr)):
        arr[i] = arr[i].capitalize()
    return ''.join(arr)


print(to_camel_case(text))
