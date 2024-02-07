# Напишіть програму, яка приймає два цілих числа від
# користувача і виводить суму діапазону чисел між ними.

# варіант 1

def sum_range(num1, num2):
    total_sum = num1 + num2
    return total_sum

num1 = int(input("Введіть перше ціле число: "))
num2 = int(input("Введіть друге ціле число: "))

print(f"Сума діапазону чисел між {num1} і {num2} дорівнює: {sum_range(num1, num2)}")

# варіант 2
def sum_diap(num1, num2):
    start = min(num1, num2)
    end = max(num1, num2)

    total_sum = 0

    for num in range(start + 1, end):
        total_sum += num

    return total_sum


num1 = int(input("Введіть перше ціле число: "))
num2 = int(input("Введіть друге ціле число: "))

print(f"Сума діапазону чисел між {num1} і {num2} дорівнює: {sum_diap(num1, num2)}")





