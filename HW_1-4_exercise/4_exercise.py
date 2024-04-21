from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Конвертуємо дату народження з рядка у об'єкт datetime.date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Визначаємо різницю між днем народження та сьогоднішнім днем
        days_until_birthday = (birthday.replace(year=today.year) - today).days

        # Перевіряємо, чи день народження випадає на наступний тиждень
        if 0 <= days_until_birthday <= 7:
            # Якщо день народження випадає на вихідний, переносимо його на наступний понеділок
            if days_until_birthday == 0 and today.weekday() >= 5:  # Сьогодні і субота/неділя
                # Додаємо різницю між понеділком (0) і останнім вихідним
                days_until_birthday += (7 - today.weekday())
            congratulation_date = today + timedelta(days=days_until_birthday)
            upcoming_birthdays.append(
                {"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays


# Приклад виконання:
users = [
    {"name": "Viktor Lisov", "birthday": "1985.04.19"},
    {"name": "Lilia Anisimova", "birthday": "2000.04.23"},
    {"name": "Dmitrii Filipof", "birthday": "2024.04.24"},
    {"name": "Nikola Rvanov", "birthday": "1990.01.27"},
    {"name": "Anrey Oldest", "birthday": "1690.04.25"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
