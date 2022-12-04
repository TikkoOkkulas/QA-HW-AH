
# 1:
print("1) Пользователь вводит слово, \
если это слово является полиндромом, то вывести '+', иначе '-'")
pol = input("введіть поліндром: ")
rev_pol = pol[::-1]
if pol == rev_pol:
    print('+')
else:
    print('-')

# 2:
print("2) Пользователь вводит текст и слово которое нужно найти, \
если это слово есть в тексте, вывести 'YES', иначе 'NO'")
text = input("введіть текст: ")
word = input("введіть слово яке є в тексті: ")
if text.find(word) != -1:
    print("YES")
else:
    print("NO")
# 3:
print("3) Пользователь вводит строку. Если она начинается на 'abc', \
то заменить их на 'www', иначе добавить в конец строки 'zzz'.'")
str = input("введіть строку: ")
if str.startswith("abc"):
    edited_str = str.replace("abc", "www", 1)
else:
    edited_str = str + "zzz"
print(edited_str)

# 4:
print("4) Пользователь вводит текст, удалить в \
тексте все цифры и вывести строку пользователю.")
text_num = input("введіть текст з цифрами чи без: ")
for char in text_num:
    if not char.isdigit():
        print(char, end ="")

# 5:
print("5) Написать валидатор для почты. Пользователь вводит почту, \
а программа должна проверить, что в почте есть символ '@' и '.', \
и если это так, то вывести 'YES', иначе 'NO'")

addr = input("введіть пошту: ") #i@b.ua
if addr.count("@") == 1 and addr[0] != "@" \
        and addr.count(".") > 0 and addr[-1] != "." \
        and addr.find("@" + 1) < addr.find("."):
                print("YES")
else:
        print("NO")


