import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # required by ALX
    return formatted_date  # ALX wants RETURN, not print

# Display the formatted date (optional print)
print(display_current_datetime())

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    now = datetime.date.today()
    future_date = now + timedelta(days=number_of_days)
    formatted_future = future_date.strftime("%Y-%m-%d")  # required by ALX
    return formatted_future  # ALX wants RETURN

# Print the returned formatted future date
print(calculate_future_date())
