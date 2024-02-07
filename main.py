# 6. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише рядки, які містять слово "Python".

def line_python(lines):
    return [line for line in lines if "Python" in line]

user_lines = []
n = int(input("Введіть кількість рядків: "))
for i in range(n):
    user_line = input("Введіть рядок {}: ".format(i + 1))
    user_lines.append(user_line)

filtered_lines = line_python(user_lines)

print("Новий список, що містить лише рядки, що містять слово 'Python':")
for line in filtered_lines:
    print(line)







