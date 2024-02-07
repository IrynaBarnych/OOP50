# 5. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери.

def function_user(words):
    return [word for word in words if word[0].isupper()]

user_words = []
n = int(input("Введіть кількість рядків: "))
for i in range(n):
    user_string = input("Введіть рядок {}: ".format(i + 1))
    user_words.append(user_string)

list = function_user(user_words)

print("новий список, що містить лише рядки, що починаються з великої літери:")
for word in list:
    print(word)






