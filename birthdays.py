from datetime import datetime, timedelta
from collections import defaultdict


def main():
  
    users= [
        {'name' : 'Bill', 'birthday' : datetime(year=2022, month=10, day=24)},
        {'name' : 'John', 'birthday' : datetime(year=2022, month=10, day=24)},
        {'name' : 'Kate', 'birthday' : datetime(year=2022, month=10, day=25)},
        {'name' : 'Alisha', 'birthday' : datetime(year=2022, month=10, day=26)},
        {'name' : 'Julie', 'birthday' : datetime(year=2022, month=10, day=27)},
        {'name' : 'Sabina', 'birthday' : datetime(year=2022, month=10, day=28)},
        {'name' : 'Anna', 'birthday' : datetime(year=2022, month=10, day=29)},
        {'name' : 'Emma', 'birthday' : datetime(year=2022, month=10, day=30)},
        {'name' : 'Charles', 'birthday' : datetime(year=2022, month=10, day=31)}
    ]

    get_birthdays_per_week(users)


def get_birthdays_per_week(users):

    current_datetime = datetime.now()
    
    delta = timedelta(days=7)

    names = []

    day_of_week = []
    
    result = defaultdict(list)

    for user in users:
        name = user.get('name')
        birth = user.get('birthday')
        difference = birth - current_datetime

        if difference <= delta:       
        
            if difference <= delta and birth.strftime('%A') == 'Saturday': 
                birth = birth + timedelta(days=2)

            elif difference <= delta and birth.strftime('%A') == 'Sunday':
                birth = birth + timedelta(days=1)

            names.append(name)
            day_of_week.append(birth)

    for d, n in zip(day_of_week, names):
        result[d].append(n)
   
    for key, value in result.items():
        printed_key = key.strftime("%A")
        lst_of_names = ', '.join(value)
        print(f'{printed_key}: {lst_of_names}')


if __name__ == '__main__':
    main()
    quit()