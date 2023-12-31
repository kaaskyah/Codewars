# Создать функцию, возвращающую сумму двух наименьших положительных чисел, 
# заданную массивом из минимум 4 положительных целых чисел. 
# Никаких плавающих или неположительных целых чисел передаваться не будет.

# Например, при передаче массива вида [19, 5, 42, 2, 77] на выходе должно получиться 7.

# При передаче массива [10, 343445353, 3453445, 3453545353453] должно быть возвращено 3453455.

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])