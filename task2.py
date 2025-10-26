import random

# генерує відсортований список випадкових чисел у заданому діапазоні
def get_numbers_ticket(min_val: int, max_val: int, quantity: int) -> list[int]:
    # перевірка вхідних даних
    if min_val < 1:
        return []
    if max_val > 1000:
        return []
    if quantity > (max_val - min_val + 1) or quantity <= 0:
        return []
    
    # використовуємо .sample для вибору унікальних номерів
    result = random.sample(range(min_val, max_val + 1), quantity)
    result.sort()
    
    return result
