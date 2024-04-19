import re


def normalize_phone(phone_number):
    # Видалаленн всі символів, крім цифр та '+'
    phone_number = re.sub(r'\D', '', phone_number)

    # Додається міжнародний код, якщо він відсутній
    if not phone_number.startswith('+'):
        if phone_number.startswith('380'):
            phone_number = '+' + phone_number
        else:
            phone_number = '+38' + phone_number

    return phone_number


# Так працює код:           наданий формат номерів   виправлений формат
print(normalize_phone("+38(050)123-32-34"))      # +380501233234
print(normalize_phone("     0503 451234"))       # +380503451234
print(normalize_phone("(0 50)88899   00"))       # +380508889900
print(normalize_phone("38050-111-2 2-2    2"))   # +380501112222
print(normalize_phone("    38050 111 22 11   "))  # +380501112211
