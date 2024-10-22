import math


def format_time(time:float):
    'Converts a floating point time value into the form M:SS:MS'

    if time < 0: calc_time = -time
    else: calc_time = round(time, 2)
    mins = math.floor(calc_time//60)
    secs = math.floor(calc_time%60)
    ms = round(round(calc_time-math.floor(calc_time), 2)*100)

    timestr = f'{mins}:{secs:02d}:{ms:02d}'
    if time < 0: timestr = '-'+timestr

    return timestr