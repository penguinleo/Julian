def Julian(Date):
    import math
# this code was translated from matlab
    year    = Date['year']
    month   = Date['month']
    day     = Date['day']
    hour    = Date['hour']
    minute  = Date['minute']
    second  = Date['second']
    print (Date)
# this function calculate the Julian day number at 0 UT for any year between 1900 and 2100

    day     = day + (hour + minute/60 + second/3600) / 24
    j0      = 365*year - int(7*(year + int((month + 9)/12))/4) + int(275*month/9) + day + 1721013.5
    return j0