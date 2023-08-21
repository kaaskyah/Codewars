# Ваша задача - отсортировать заданную строку. Каждое слово в строке будет содержать одно число.
# Это число - позиция, которую слово должно занимать в результате.

# Примечание: Числа могут быть от 1 до 9. Поэтому 1 будет первым словом (а не 0).

# Если входная строка пуста, то возвращается пустая строка.
# Слова во входной строке будут содержать только правильные последовательные числа.

# Примеры
# "is2 Thi1s T4est 3a" --> "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2" --> "Fo1r the2 g3ood 4of th5e pe6ople"
# "" --> ""

def giveNum(s):
    for i in str(s):
        if i in '123456789':
            return int(i)


def order(sentence):
    res = ['0'] * len(sentence.split())
    for i in sentence.split():
        res[giveNum(i)-1] = i
    return ' '.join(res)


print(order('fr2 hti3gi rt1'))
