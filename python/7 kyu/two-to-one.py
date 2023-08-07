# Возьмем две строки s1 и s2, содержащие только буквы от a до z. 
# Вернем новую отсортированную строку, максимально длинную, содержащую отдельные буквы, 
# каждая из которых взята только один раз, из s1 или s2.

# Примеры:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(a1, a2):
    return ''.join(sorted(set(a1+a2)))