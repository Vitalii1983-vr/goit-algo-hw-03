
# 1. Імпорт модуля datetime
from datetime import datetime

# Створення функції get_days_from_today


def get_days_from_today(date):
    try:
        # 2. Перетворення рядка дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        # Отримання поточної дати, використовуючи datetime.today()
        current_date = datetime.today().date()
        # Розрахунок різниці між поточною датою та заданою датою
        difference = (current_date - target_date).days
        return difference
    # Обробка винятків у разі неправильного формату вхідних даних
    except ValueError:
        # Обробка винятку у випадку неправильного формату вхідних даних
        print("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")
        return None


# Поверненнчя різниці у днях як ціле число
print(get_days_from_today("2022-02-24"))  # Повинно вивести 785
