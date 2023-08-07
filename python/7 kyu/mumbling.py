# На этот раз без истории и теории. Приведенные ниже примеры показывают,
# как писать функции accum:

# Примеры:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# Параметром accum является строка, включающая только буквы от a..z и A..Z.

def accum(s):
    res = []
    for i in range(1, len(s)+1):
        res.append((s[0]*i).capitalize())
        s = s[1:]
    return '-'.join(res)