from datetime import datetime
def get_days_from_today(date_str: str) -> int:
    date_format = "%Y-%m-%d"
    try:
        parsed_date = datetime.strptime(date_str, date_format).date()
    except ValueError:
        print(f"Неправильний формат дати: '{date_str}'. Використовуйте 'РРРР-ММ-ДД'")
        return 0 
    today_date = datetime.today().date()
    return (today_date - parsed_date).days