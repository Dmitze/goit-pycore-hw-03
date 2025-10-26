from datetime import datetime


# функція для розрахунку різниці в днях від заданої дати
# має повертати ціле число як результат 
def get_days_from_today(date_str: str) -> int:

    # очікуваний формат дати
    date_format = "%Y-%m-%d"

    try:
        # перетворюємо рядок на об'єкт datetime
        parsed_date = datetime.strptime(date_str, date_format).date()
    except ValueError:
        # якщо формат невірний, виводимо попередження
        print(f"Неправильний формат дати: '{date_str}'. Використовуйте 'РРРР-ММ-ДД'")
        return

    today_date = datetime.today().date()

    # повертаємо різницю у днях
    return (today_date - parsed_date).days