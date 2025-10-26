from datetime import datetime, date, timedelta


# очікує список користувачів з іменами та днями народження у форматі 'РРРР.ММ.ДД'
def get_upcoming_birthdays(users: list):
    
    today = datetime.today().date()
    birthdays = []

    for user in users:
        try:
            bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            
            birthday_this_year = bday.replace(year=today.year)

            # якщо день народження вже минув, дивимось на наступний рік
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            delta_days = (birthday_this_year - today).days

            if 0 <= delta_days < 7:
                congratulation_date = birthday_this_year
                # якщо день народження на вихідних, переносимо на понеділок
                day_of_week = congratulation_date.weekday()
                
                if day_of_week == 5: # Субота
                    congratulation_date += timedelta(days=2)
                elif day_of_week == 6: # Неділя
                    congratulation_date += timedelta(days=1)
                
                birthdays.append({
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
                })

        except ValueError:
            continue

    return birthdays

users_data = [
    {"name": "Олена", "birthday": "1990.10.15"}, 
    {"name": "Іван", "birthday": "1988.10.18"},  
    {"name": "Марія", "birthday": "1995.10.19"}, 
    {"name": "Петро", "birthday": "1980.10.20"}, 
]

upcoming_birthdays = get_upcoming_birthdays(users_data)
print("Кого вітати:")

sorted_birthdays = sorted(upcoming_birthdays, key=lambda x: x['congratulation_date'])
for entry in sorted_birthdays:
    print(f" - {entry['name']}: {entry['congratulation_date']}")