"""
input date format = YYYY-mm-dd
"""
from date_utils.calculations import *

date_format = 'yyyy-mm-dd'
start_date = input(f'enter date in the format {date_format} : ')
end_date = input(f'enter end date in the format {date_format} : ')

print(f'the days between the date is {days_between(start_date, end_date)}')

date = input(f"enter the date in the format {date_format} : ")
days = int(input('enter the number of days needed to be added : '))
print(f'the date after {days} days : {add_days(date, days)}')