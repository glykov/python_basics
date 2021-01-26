# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from google_trans_new import google_translator

translator = google_translator()
translation = []

infile = open('text_4.txt', 'r', encoding='utf8')
outfile = open('ru_text_4.txt', 'w', encoding='utf8')

for line in infile:
    words = line.split()
    ru_word = translator.translate(words[0], lang_src='en', lang_tgt='ru')
    translation.append(" ".join([ru_word.strip(), words[1], words[2]]) + '\n')

outfile.writelines(translation)

infile.close()
outfile.close()
