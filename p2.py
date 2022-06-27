# Solve the problem from the second set here

"""
    Non-UI functions
"""


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 1
    else:
        return 0


def set_month_name():
    return ['January', 'February', 'March', 'April', 'May', 'June', 'July',
            'August', 'September', 'October', 'November', 'December']


def set_month_days(year):
    """
    Returns a list with the number of days for each month based on the year
    """
    if is_leap_year(year):
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def find_day(month_index, month_days, days):
    """
    Finds the active day in the month, by subtracting the number of days from the previous months
    :param month_index: The current month
    :param month_days: The list with the number of days for each month
    :param days: The number of days in the year
    :return: The current day in the month
    """
    for i in range(0, month_index):
        days -= month_days[i]
    return days


def find_month(month_days, days):
    """
    Returns the month we are in
    :param month_days: The list with the number of days for each month
    :param days: The number of days in the year
    """
    i = 0  # we start to count days from 0
    for month_index in range(0, 12):
        i += month_days[month_index]
        if i >= days:
            # that means the current date is included in this month
            return month_index


def find_date(days, year):
    """
    Find date based on parameters
    :param days: The number of days in the year
    :param year: The actual year
    :return: Creates a string that contains the correct date
    """
    month_days = set_month_days(year)
    month_index = find_month(month_days, days)
    month_name = set_month_name()
    day = find_day(month_index, month_days, days)

    answer = 'Now is ' + str(year) + ', ' + month_name[month_index] + ' ' + str(day)
    if day % 10 == 1 and day // 10 != 1:
        answer += 'st'
    elif day % 10 == 2 and day // 10 != 1:
        answer += 'nd'
    elif day % 10 == 3 and day // 10 != 1:
        answer += 'rd'
    else:
        answer += 'th'

    return answer


def check_date(date):
    days = date[0]
    year = date[1]

    if year < 0:
        return 0
    else:
        if is_leap_year(year) and (days > 366 or days <= 0):
            return 0
        elif not is_leap_year(year) and (days > 365 or days <= 0):
            return 0
    return 1


"""
    UI functions
"""


def read_input():
    year = int(input("Tell me the year: "))
    days = int(input("Tell me the day: "))
    return days, year


def print_date(days, year):
    print(find_date(days, year))


def start():
    date = read_input()
    if check_date(date):
        print_date(date[0], date[1])
    else:
        print("Invalid date!")


start()
