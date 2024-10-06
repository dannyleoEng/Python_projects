def cal_register_percent(school_days: int, total_pupil: int) -> None:
    count = 0
    key = []
    value = []
    value2 = []
    
    for number in range(school_days):
        count += 1
        days = f'Day{count}'
        key.append(days)
        number_of_pupil = int(input(f"How many student came on {days} (morning): "))
        number_of_afternoon_pupils = int(input(f"How many student came on {days} (afternoon): "))
        value.append(number_of_pupil)
        value2.append(number_of_afternoon_pupils)
    total_value_morning = 0
    for items in value:
        total_value_morning += items
    total_value_afternoon = 0
    for items in value2:
        total_value_afternoon += items
    values = [x + y for x, y in zip(value, value2)]
    print(f'How many school days for the week: {school_days} days')
    total_attendance = total_value_morning + total_value_afternoon
    calculate_percent = total_attendance * 100
    school_days = school_days * 2
    result = (calculate_percent / school_days / total_pupil)
    my_dict = dict(zip(key, values))
    print(f'Total number of students in the Morning: {total_value_morning} students')
    print(f'Total number of students in the afternoon: {total_value_afternoon} students')
    for keys in my_dict:
        print(f'{keys}: {my_dict[keys]} students attended school in the morning and afternoon')
    print(f'The Total result percentage: {result:.2f}%')


def main() -> None:
    try:
        total_pupil = int(input('Total Pupils: '))
        school_days = int(input('Total school days: '))
        cal_register_percent(school_days, total_pupil)
    except ValueError as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()
