import random


def get_numbers_ticket(min_num, max_num, quantity):
    # Перевірка валідності вхідних даних
    if not all(isinstance(x, int) for x in [min_num, max_num, quantity]):
        print("Параметри повинні бути цілими числами.")
        return []
    if min_num < 1 or max_num > 1000 or min_num >= max_num or quantity < 1 or quantity > (max_num - min_num + 1):
        print("Неправильні параметри. Перевірте, що min менше max та кількість в межах від min до max.")
        return []

    # Генерування унікальних випадкових чисел
    numbers = random.sample(range(min_num, max_num + 1), quantity)
    numbers.sort()  # Відсортувати числа

    return numbers


# Приклад використання:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
