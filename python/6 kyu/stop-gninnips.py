# Напишите функцию, которая принимает строку из одного или нескольких слов 
# и возвращает ту же строку, но с перевернутыми словами из пяти или более букв 
# (как в названии этого Ката). Передаваемые строки будут состоять только из букв и пробелов. 
# Пробелы будут включены только в том случае, если в строке присутствует более одного слова.

# Примеры:

# spinWords("Hey fellow warriors" ) => возвращает "Hey wollef sroirraw". 
# spinWords("This is a test") => возвращает "This is a test". 
# spinWords("Это еще один тест" )=> возвращает "Это тест rehtona"

def spin_words(sentence):
    res = []
    for i in sentence.split():
        if len(i) < 5:
            res.append(i)
        else:
            res.append(i[::-1])
    return ' '.join(res)