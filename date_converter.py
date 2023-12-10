from datetime import datetime, timedelta

__version__ = "1.2.0"

def convert_five_digit_number_to_date(five_digit_number):
    # Define the base date (1900-01-01)
    base_date = datetime(1900, 1, 1)
    
    # Calculate the number of days to add to the base date
    days_to_add = five_digit_number
    
    # Calculate the new date
    result_date = base_date + timedelta(days=days_to_add)
    
    return result_date

# Example usage
five_digit_number = 0
result = convert_five_digit_number_to_date(five_digit_number)
print(f"Converted date from ({five_digit_number}) 5D Bitcoin Digit : {result.strftime('%Y-%m-%d')}")


def convert_date_to_five_digit_number(date_string):
    # Convert the date string to a datetime object
    date_object = datetime.strptime(date_string, '%Y-%m-%d')
    
    # Calculate the number of days elapsed between the base date (1900-01-01) and the target date
    base_date = datetime(1900, 1, 1)
    days_elapsed = (date_object - base_date).days
    
    return days_elapsed

# Example usage
date_string = '1900-01-01'
result = convert_date_to_five_digit_number(date_string)
print(f"Converted 5D Bitcoin Digit from ({date_string}) date: {result}")
