ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
on = False
def is_valid_d(d):
    while d != '1' and d != '2':
        d = input('Выберите 1 если шифровать или 2 если дешифровать')
    else:
        if d == '1':
            return True
        else:
            return False
def is_valid_l(l):
    while l != 'русский' and l != 'английский':
        l = input('Введите русский или английский')
    else:
        if l == 'русский':
            return True
        else:
            return False
def is_valid_s(s):
    while s.isalpha() or s == '0':
        s = input('Введите число! (Не 0)')
    else:
        return s
d = input('Вы хотите шифровать текст или дешифровать? Нажмите 1 или 2')
d = is_valid_d(d)
l = input('Язык алфавита? [русский] или [английский]').lower()
l = is_valid_l(l)
s = input('Шаг сдвига? (Не 0)')
s = int(is_valid_s(s))
if d:
    if l:
        text = [i for i in input('Введите желаемый текс')]
        for i in range(len(text)):
            if text[i].isalnum() and not(text[i].isdigit()):
                if not(text[i] in ru):
                    on = True
                else:
                    on = False
                if s > 0:
                    if(ru.index(text[i].lower()) + s) < 32:
                        text[i] = ru[ru.index(text[i].lower()) + s]
                    else:
                        text[i] = ru[ru.index(text[i].lower()) + s - 32]
                else:
                    if (ru.index(text[i].lower()) + s) > -1:
                        text[i] = ru[ru.index(text[i].lower()) + s]
                    else:
                        text[i] = ru[ru.index(text[i].lower()) + 32 + s]
                if on:
                    text[i] = text[i].upper()
    else:
        text = [i for i in input('Введите желаемый текс')]
        for i in range(len(text)):
            if text[i].isalnum() and not(text[i].isdigit()):
                if not(text[i] in en):
                    on = True
                else:
                    on = False
                if s > 0:
                    if(en.index(text[i].lower()) + s) < 26:
                        text[i] = en[en.index(text[i].lower()) + s]
                    else:
                        text[i] = en[en.index(text[i].lower()) + s - 26]
                else:
                    if (en.index(text[i].lower()) + s) > -1:
                        text[i] = en[en.index(text[i].lower()) + s]
                    else:
                        text[i] = en[en.index(text[i].lower()) + 26 + s]
                if on:
                    text[i] = text[i].upper()
else:
    if l:
        text = [i for i in input('Введите желаемый текс')]
        for i in range(len(text)):
            if text[i].isalnum() and not(text[i].isdigit()):
                if not(text[i] in ru):
                    on = True
                else:
                    on = False
                if s > 0:
                    if(ru.index(text[i].lower()) - s) < 32:
                        text[i] = ru[ru.index(text[i].lower()) - s]
                    else:
                        text[i] = ru[ru.index(text[i].lower()) - s - 32]
                else:
                    if (ru.index(text[i].lower()) - s) > -1:
                        text[i] = ru[ru.index(text[i].lower()) - s]
                    else:
                        text[i] = ru[ru.index(text[i].lower()) + 32 - s]
                if on:
                    text[i] = text[i].upper()
    else:
        text = [i for i in input('Введите желаемый текс')]
        for i in range(len(text)):
            if text[i].isalnum() and not(text[i].isdigit()):
                if not(text[i] in en):
                    on = True
                else:
                    on = False
                if s > 0:
                    if(en.index(text[i].lower()) - s) < 26:
                        text[i] = en[en.index(text[i].lower()) - s]
                    else:
                        text[i] = en[en.index(text[i].lower()) - s - 26]
                else:
                    if (en.index(text[i].lower()) - s) > -1:
                        text[i] = en[en.index(text[i].lower()) - s]
                    else:
                        text[i] = en[en.index(text[i].lower()) + 26 - s]
                if on:
                    text[i] = text[i].upper()
print(*text, sep = '')
