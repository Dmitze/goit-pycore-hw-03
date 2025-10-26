import re

def normalize_phone(phone_number: str) -> str:

    # прибираємо всі символи окрім цифр та '+'
    pattern = r"[^\d\+]"
    sanitized_number = re.sub(pattern, "", phone_number)

    # тепер перевіряємо, як виглядає номер
    if sanitized_number.startswith('380'):
        # якщо він починається з 380, то просто додаємо + попереду
        return '+' + sanitized_number
    elif sanitized_number.startswith('0'):
        # якщо з 0, то додаємо міжнародний код +38
        return '+38' + sanitized_number
    else:
        # якщо номер вже має +, то нічого не робимо
        if sanitized_number.startswith('+'):
            return sanitized_number
        else:
            # в іншому випадку, вважаємо, що код країни відсутній
            return '+38' + sanitized_number