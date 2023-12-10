from datetime import datetime

def convert_date_to_five_digit_number(date_string):
    # Dátum sztring átalakítása dátum objektummá
    date_object = datetime.strptime(date_string, '%Y-%m-%d')
    
    # Az alapdátum (1900-01-01) és a cél dátum között eltelt napok számának kinyerése
    base_date = datetime(1900, 1, 1)
    days_elapsed = (date_object - base_date).days + 2
    
    return days_elapsed

# Példa használat
date_string = '2010-05-22'
result = convert_date_to_five_digit_number(date_string)
print(result)
