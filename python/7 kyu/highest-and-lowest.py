# В этом небольшом задании вам дается строка чисел, разделенных пробелами, 
# и вы должны вернуть наибольшее и наименьшее число.

# Примеры
# highAndLow("1 2 3 4 5"); // возвращается "5 1"
# highAndLow("1 2 -3 4 5"); // возвращается "5 -3"
# highAndLow("1 9 3 4 -5"); // возвращается "9 -5"
# Примечания
# Все числа являются допустимыми Int32, проверять их не нужно.
# Во входной строке всегда будет хотя бы одно число.
# Выходная строка должна состоять из двух чисел, разделенных одним пробелом, причем первым должно быть наибольшее число.

def high_and_low(numbers):
    res = [int(s) for s in numbers.split()]
    return str(max(res)) + ' ' + str(min(res))