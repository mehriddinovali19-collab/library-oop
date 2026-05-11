from string import digits

def validate_user(username: str) -> tuple[bool, str]:
    if " " in username:
        return False, "Username bosh joylardan iborat bo'lmasligi kerak."
    elif not username.isalpha():
        return False, "Username faqat harflardan iborat bo'lishi kerak."
    elif not username.islower():
        return False, "Username kichik harflardan iborat bo'lishi kerak."
    else: 
        return True, ""
    


def validate_password(password: str):
    if len(password) <= 4:
        return False, "Password kamida 4 ta belgidan iborak bolsin"
    
    digit_count = 0
    for digit in digits:
        if digit.isdigit():
            digit_count += 1

    if digit_count == 0:
        return False, "Password kamida bitta raqamdan iborat bo'lishi kerak."
    
    return True, ""
    

def nomalize_full_name(full_name: str) -> str:
    return full_name.title()
    