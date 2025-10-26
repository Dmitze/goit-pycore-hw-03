from datetime import datetime, date, timedelta


# очікує список користувачів з іменами та днями народження у форматі 'РРРР.ММ.ДД'
def get_upcoming_birthdays(users: list):

    name_key = "name"
    birthday_key = "birthday"
    congratulation_date_key = "congratulation_date"
    birthday_pattern = "%Y.%m.%d"
    upcoming_range = 7
    saturday = 5 # weekday() для суботи це 5
    sunday = 6 # weekday() для неділі це 6

    current_date = datetime.today().date()
    
    celebration_list = []

    # ітеруємо по користувачах
    for user in users:
        # парсимо дату народження
        birthday_date = datetime.strptime(user[birthday_key], birthday_pattern).date()
        
        # визначаємо дату святкування цього року
        this_year_birthday_date = birthday_date.replace(year=current_date.year)

        if this_year_birthday_date < current_date:
            # якщо день народження вже минув, дивимось на наступний рік
            congrats_date = this_year_birthday_date.replace(year=current_date.year + 1)
        else:
            congrats_date = this_year_birthday_date

        # перевіряємо, чи потрапляє дата у наш 7-денний діапазон
        delta_days = (congrats_date - current_date).days
        if 0 <= delta_days < upcoming_range:

            # переносимо дату, якщо це вихідний
            congrats_day_of_week = congrats_date.weekday()
            if congrats_day_of_week == saturday:
                congrats_date = congrats_date + timedelta(days=2)
            elif congrats_day_of_week == sunday:
                congrats_date = congrats_date + timedelta(days=1)

            celebration_list.append({name_key: user[name_key], congratulation_date_key: congrats_date.strftime(birthday_pattern)})

    return celebration_list