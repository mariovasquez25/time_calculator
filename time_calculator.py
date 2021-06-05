def add_time(start, duration, dayWeek=""):

    if dayWeek != "":
        print('-->', start, '+', duration, 'hours, of the day', dayWeek.capitalize())
    else:
        print('-->', start, '+', duration, 'hours.')

    meridiano = start.split()[1]
    hourMin = start.split()[0].split(':')
    duraSp = duration.split(':')
    meridiano_2 = ""
    num = 0

    days_weeks = ['Monday', 'Tuesday', 'Wednesday',
                  'Thursday', 'Friday', 'Saturday', 'Sunday']
    week = dayWeek.capitalize()
    idx = days_weeks.index(week) if dayWeek != "" else None

    hour = int(hourMin[0]) + int(duraSp[0])
    min = int(hourMin[1]) + int(duraSp[1])

    if min > 60:
        min -= 60
        hour += 1

    days = round((hour / 24) + 0.5)

    if dayWeek != "" and days > 1:

        count = 0

        while True:

            count += 1
            idx += 1

            if idx >= len(days_weeks):
                idx = 0

            if count == days:
                break

        dayWeek = ', ' + days_weeks[idx]

    if hour >= 12:
        num = hour // 12

        hour = (hour - 12 * (hour // 12 - 1)) - 12
        if hour == 0:
            hour = 12

    if num % 2 != 0 and meridiano == 'AM':
        meridiano_2 = 'PM'
    elif num % 2 != 0 and meridiano == 'PM':
        meridiano_2 = 'AM'
    else:
        meridiano_2 = meridiano

    if days == 1 and meridiano == 'PM' and meridiano_2 == 'AM' or duration == '24:00':
        days = ' (next day)'

        if dayWeek != "":
            dayWeek = ', Monday' if days_weeks.index(
                week) == 6 else ', ' + days_weeks[days_weeks.index(week) + 1]

    elif days > 1:
        days = ' (' + str(days) + ' days later)'

    else:
        days = ''
        dayWeek = ', ' + days_weeks[idx] if dayWeek != "" else ""

    hour = str(hour)
    min = str(min).zfill(2) if min < 10 else str(min)

    new_time = hour + ':' + min + ' ' + meridiano_2 + dayWeek + days

    return new_time
