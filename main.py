from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
import emoji
def data():
    current_datetime = datetime.datetime.now()
    current_year = current_datetime.year
    current_month = current_datetime.month
    current_day = current_datetime.day
    s = f"Текущий год: {current_year}\nТекущий месяц: {current_month}\nТекущий день: {current_day} "
    return s

if __name__ == '__main__':
    print(calculate_salary())
    print(get_employees())
    print(data())
    print(emoji.emojize('Python is :fire:'))