import re

def normalize_phone(phone_number: str) -> str:
    pattern = r"[^\d\+]"
    p = re.sub(r'\D', '', phone_number)
    
    if len(p) == 12 and p.startswith('380'):
        return '+' + p
    elif len(p) == 10 and p.startswith('0'):
        return '+38' + p
    else:
        return '+38' + p.lstrip('38')