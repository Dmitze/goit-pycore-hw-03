import random

def get_numbers_ticket(min_val: int, max_val: int, quantity: int) -> list[int]:
    is_valid = 1 <= min_val <= max_val <= 1000 and 0 < quantity <= (max_val - min_val + 1)
    if not is_valid:
        return []
    
    result = random.sample(range(min_val, max_val + 1), quantity)
    result.sort()
    
    return result
