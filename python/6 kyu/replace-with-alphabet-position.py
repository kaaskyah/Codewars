# В этом ката требуется, задав строку, заменить каждую букву на ее позицию в алфавите.

# Если что-то в тексте не является буквой, игнорируйте это и не возвращайте.

# "a" = 1, "b" = 2 и т.д.

# Пример
# alphabetPosition("Закат солнца наступает в двенадцать часов").
# Должно вернуть "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (в виде строки)

from string import *
def alphabet_position(text):
    poz, text, res = list((ascii_lowercase)), text.lower(), ''
    for i in text:
        if i in poz:
            res += str(poz.index(i)+1) + ' '
    return res[:-1]