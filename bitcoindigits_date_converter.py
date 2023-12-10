from datetime import datetime, timedelta

__version__ = "2.0.0"


def is_valid_date(year, month, day):
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False

def is_valid_date_input(date_input):
    try:
        parsed_date = datetime.strptime(date_input, "%Y-%m-%d")
        return is_valid_date(parsed_date.year, parsed_date.month, parsed_date.day)
    except ValueError:
        return False

def convert_five_digit_number_to_date(five_digit_number):
    # Define the base date (1900-01-01)
    base_date = datetime(1900, 1, 1)
    
    # Calculate the number of days to add to the base date
    days_to_add = five_digit_number
    
    # Calculate the new date
    result_date = base_date + timedelta(days=days_to_add)
    
    return result_date

def convert_date_to_five_digit_number(date):
    # Define the base date (1900-01-01)
    base_date = datetime(1900, 1, 1)

    # Calculate the difference in days
    delta = date - base_date
    days_difference = delta.days

    return days_difference

def get_numeric_value(s):
    return int(s.lstrip('0')) if s.lstrip('0') else 0

def permute_string(s):
    if len(s) == 0:
        return ['']
    prev_list = permute_string(s[1:])
    next_list = []
    for i in range(len(prev_list)):
        for j in range(len(s)):
            new_str = prev_list[i][:j] + s[0] + prev_list[i][j:]
            if new_str not in next_list:
                next_list.append(new_str)
    return next_list

def get_valid_date_input():
    valid_start_date = datetime(1900, 1, 1)
    valid_end_date = datetime(2173, 10, 15)

    while True:
        date_input = input(f"---- Please enter a valid formate date (YYYY-MM-DD) between {valid_start_date.strftime('%Y-%m-%d')} and {valid_end_date.strftime('%Y-%m-%d')}\n")

        if is_valid_date_input(date_input):
            parsed_date = datetime.strptime(date_input, "%Y-%m-%d")

            if valid_start_date <= parsed_date <= valid_end_date:
                return parsed_date
            else:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - The valid period is between {valid_start_date.strftime('%Y-%m-%d')} and {valid_end_date.strftime('%Y-%m-%d')}.\n")
        else:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Invalid format or date! Please enter a valid date (YYYY-MM-DD).\n")

# Welcome message for the first part
print("Welcome to the 5D Bitcoin digits date converter!")
print("This program allows you to convert dates to 5D Bitcoin Digit numbers and vice versa!")
print("Follow us on twitter: https://twitter.com/BitcoinDigits or our website: https://bitcoindigits.com/ \n")

# Test the function for the first part
try:
    # Get valid date input
    valid_date = get_valid_date_input()
    print(f"Valid date: {valid_date.strftime('%Y-%m-%d')}")

    # Convert date to five-digit number
    five_digit_number = convert_date_to_five_digit_number(valid_date)
    print(f"The valid date converted to a 5D Bitcoin Digit: {five_digit_number}\n")

except ValueError as ve:
    print(f"Error: {ve}")

# Second part
try:
    # Get valid five-digit number input
    while True:
        input_number = input("----Please enter a 5D Bitcoin Digit number between 00000 and 99999 (enter 0 to exit):\n")

        if input_number == '0':
            break

        if input_number.isdigit() and len(input_number) == 5 and 0 <= int(input_number) <= 99999:
            numeric_value = get_numeric_value(input_number)
            permutations = permute_string(input_number)
            date_value = convert_five_digit_number_to_date(numeric_value)
            print(f"The number {input_number} corresponds to the date: {date_value.strftime('%Y-%m-%d')}\n")
            break
        else:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Invalid format! Please enter a valid 5D Bitcoin Digit number between 00000 and 99999.\n")
except ValueError as ve:
    print(f"Error: {ve}")

print("\n_________________________________________")
print("To convert new dates, rerun the script!!!")
