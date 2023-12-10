__version__ = "1.0.0"

from datetime import datetime, timedelta

def convert_five_digit_number_to_date(five_digit_number):
    # Define the base date (1900-01-01)
    base_date = datetime(1900, 1, 1)
    
    # Calculate the number of days to add to the base date
    days_to_add = five_digit_number - 1
    
    # Calculate the new date
    result_date = base_date + timedelta(days=days_to_add)
    
    return result_date

# Example usage
five_digit_number = 1
result = convert_five_digit_number_to_date(five_digit_number)
print(result.strftime('%Y-%m-%d'))


def convert_date_to_five_digit_number(date_string):
    # Convert the date string to a datetime object
    date_object = datetime.strptime(date_string, '%Y-%m-%d')
    
    # Calculate the number of days elapsed between the base date (1900-01-01) and the target date
    base_date = datetime(1900, 1, 1)
    days_elapsed = (date_object - base_date).days + 1
    
    return days_elapsed

# Example usage
date_string = '1900-01-01'
result = convert_date_to_five_digit_number(date_string)
print(result)
