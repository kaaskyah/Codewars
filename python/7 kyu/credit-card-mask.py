# Обычно, когда вы что-то покупаете, вас спрашивают, верен ли номер вашей кредитной карты, 
# номер телефона или ответ на ваш самый секретный вопрос. Однако, 
# поскольку кто-то может заглянуть вам через плечо, вы не хотите, чтобы это было показано на экране. 
# Вместо этого мы маскируем его.

# Ваша задача - написать функцию maskify, которая меняет все символы, кроме последних четырех, на '#'.

# Примеры (ввод --> вывод):
# "4556364607935616" --> "############5616"
#      "64607935616" --> "#######5616"
#                "1" --> "1"
#                 "" --> ""

# // "Как звали вашего первого домашнего питомца?"
# "Skippy" --> "##ippy"
# "Nanananananananananananananananananananananananananananananananana Batman!" --> "####################################man!"

def maskify(cc):
    res = '#' * len(cc)
    if len(cc) <= 4:
        return cc
    res = res[:-4]
    res += cc[-4:]
    return res