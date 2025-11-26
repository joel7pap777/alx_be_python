import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"the current date and time:{current_date}")
display_current_datetime()

number_of_days = int(input('enter the number of days to add to the current date:'))

def calculate_future_date():
    now = datetime.date.today()
    future_date = now + timedelta(days=number_of_days)
    print(future_date)

calculate_future_date()   