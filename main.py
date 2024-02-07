# 2. Напишіть програму, для знаходження суми всіх парних чисел від 1 до 100.


total_sum = 0


for number in range(1, 101):
    if number % 2 == 0:
        total_sum += number

print("Сума всіх парних чисел від 1 до 100:", total_sum)




