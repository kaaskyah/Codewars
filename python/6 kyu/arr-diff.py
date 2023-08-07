# Ваша задача в этом ката состоит в том, чтобы реализовать функцию разности, 
# которая вычитает один список из другого и возвращает результат.

# Она должна удалять все значения из списка a, которые присутствуют в списке b, сохраняя их порядок.

# arrayDiff([1,2],[1]) == [2]
# Если значение присутствует в b, то все его вхождения должны быть удалены из другого:

# arrayDiff([1,2,2,2,3],[2]) == [1,3]

def array_diff(a, b):
    return [i for i in a if i not in b]