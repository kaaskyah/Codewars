# Джейден Смит, сын Уилла Смита, является звездой таких фильмов, как "Малыш-каратист" (2010) и "После Земли" (2013). 
# Джейден также известен своей философией, которую он излагает в Twitter. 
# Когда он пишет в Twitter, он известен тем, что почти всегда пишет каждое слово с большой буквы. 
# Для простоты вам придется писать каждое слово с заглавной буквы, 
# посмотрите, как должны выглядеть сокращения в примере ниже.

# Ваша задача - преобразовать строки в то, как они были бы написаны Джейденом Смитом. 
# Строки представляют собой реальные цитаты Джейдена Смита, но они не набраны заглавными буквами так, 
# как он набрал их в оригинале.

# Пример:

# Не Jaden-Cased: "Как зеркала могут быть настоящими, если наши глаза не настоящие".
# Jaden-Cased:     "Как могут быть реальными зеркала, если наши глаза не реальны"

def to_jaden_case(string):
    return ' '.join([i.capitalize() for i in string.split(' ')])