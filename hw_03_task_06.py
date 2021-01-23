# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
    '''принимает слово из маленьких латинских букв и возвращающет его же, но с прописной первой буквой'''
    letters = list(word)
    if 'a' <= letters[0] <= 'z':
        letters[0] = chr(ord(letters[0]) - 32)
    result = ''
    for letter in letters:
        result += letter
    return result


def capitalize_words(sentence):
    words = sentence.split()
    result = ''
    for word in words:
        result += int_func(word) + ' '
    return result.rstrip()


print(int_func('text'))
print(capitalize_words('lorem ipsum dolor sit amet consectetur adipisicing elit'))
