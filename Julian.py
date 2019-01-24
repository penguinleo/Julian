def Julian(Date):
    # Date = {"year":2018,"month":12,"day":29,"hour":19,"minute":16,"second":00,"ms":0}
    print(Date)
    year    = Date["year"]
    month   = Date["month"]
    day     = Date["day"]
    hour    = Date["hour"]
    minute  = Date["minute"]
    second  = Date["second"]
    ms      = Date["ms"]
    day     = day + (hour + minute/60 + second/3600 + ms/3600000) / 24
    # j0      = 367*year - int(7*(year + int((month + 9)/12))/4)  + int(275*month/9) + day + 1721013.5
    j0      = 367*year - int(7*(year + int((month + 9)/12))/4)  + int(275*month/9) + day + 1721013.5
    j1      = j0 * 24 * 3600
    return j1