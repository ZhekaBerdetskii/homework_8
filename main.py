from datetime import datetime, date, timedelta

users = [
    {'name': 'Margo', 'birthday': '1990-08-16'},
    {'name': 'Ben', 'birthday': '1987-08-17'},
    {'name': 'Peter', 'birthday': '1985-08-18'},
    {'name': 'Anna', 'birthday': '1991-08-19'},
    {'name': 'John', 'birthday': '1990-08-20'},
    {'name': 'Kate', 'birthday': '1995-08-21'},
    {'name': 'Tomas', 'birthday': '1993-08-22'},
    {'name': 'Tommy', 'birthday': '1985-08-22'},
    {'name': 'Arthur', 'birthday': '1992-08-24'},
    {'name': 'Meggi', 'birthday': '1987-08-25'},
    {'name': 'Barbara', 'birthday': '1985-08-26'},
    {'name': 'Jes', 'birthday': '1991-08-27'},
    {'name': 'Bob', 'birthday': '1990-08-28'},
    {'name': 'Mary', 'birthday': '1987-08-29'},
    {'name': 'Steven', 'birthday': '1985-08-30'},
    {'name': 'Jessy', 'birthday': '1991-08-31'}
]


result = {
    'Monday': [],
    'Tuesday': [],
    'Wednesday': [],
    'Thursday': [],
    'Friday': []
}

weekdays = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday'
}


def get_birthdays_per_week(data: list):
    now = datetime.now().date()
    # now = date(year=2023, month=8, day=21)
    end = now + timedelta(days=6)
    for i in data:
        y, m, d = i.get('birthday').split('-')
        birthday_date = date(year=now.year, month=int(m), day=int(d))
        wd = birthday_date.weekday()
        if wd in (5, 6) and now.weekday() == 0 and now - timedelta(days=2) <= birthday_date <= end - timedelta(days=2):
            result.get('Monday').append(i.get('name'))
        elif wd in (5, 6) and now.weekday() != 0 and now <= birthday_date <= end:
            result.get('Monday').append(i.get('name'))
        elif 0 <= wd <= 4 and now <= birthday_date <= end:
            result.get(weekdays.get(wd)).append(i.get('name'))
    for i in [now + timedelta(days=i) for i in range(0, 7)]:
        if i.weekday() not in (5, 6) and len(result[weekdays[i.weekday()]]) != 0:
            print(f'{weekdays[i.weekday()]}: {", ".join(result[weekdays[i.weekday()]])}')


get_birthdays_per_week(users)






