import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(num):
    pattern = r"[()\-\.\s\\t\\n]" #remove all unnecessary characters 
    replacement = ""
    modified_num = re.sub(pattern, replacement, num)

    if re.match(r"^380", modified_num): #add "+" to modified number if it starts from 380
        return "+" + modified_num
    elif re.match(r"^[0]\d+", modified_num): #add +380 if the modified number starts from 0
        return "+38" + modified_num
    else:
        return modified_num
    
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)






