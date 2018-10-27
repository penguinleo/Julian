MJD# Julian date to Gregorian year, month, day and fraction of a day
# this code was based on the routine of the International Astronomical Union's SOFA software collection

# Given:
# DJ1, DJ2   Julian date
# Returned:
#   year    int
#   month   int
#   day     int
#   hour    int
#   minute  int
#   second  int 

# Notes:
#   1) the earliest valid date is -68569.5 (-4900 March 1). The largest value accepted is 10^9
#   2) the Julian date is apportioned in any convenient way between the arguments DJ1 and DJ2.
#      for example, JD = 2450123.7 could be expressed in any of these ways, among others:
#           DJ1                 DJ2
#           2450123.7D0         0D0             (JD method)
#           2451545D0           -1421.3D0       (J2000 method)
#           2400000.5D0         50123.2D0       (MJD method)
#           2450123.5D0         0.2D0           