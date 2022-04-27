def alarm_clock(day, vacation):
    if vacation:
        if 1 <= day <= 5:
            return f'10:00'
        elif day == 0 or day == 6:
            return f'off'
    else:
        if 1 <= day <= 5:
            return f'7:00'
        elif day == 0 or day == 6:
            return f'10:00'


print(alarm_clock(1, False))
print(alarm_clock(5, False))
print(alarm_clock(0, False))