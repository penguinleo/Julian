from decimal import *
def Jd2Cal(j0,j1):
    from math import ceil
    
    getcontext().prec = 50
    # Julian date = j0 + j1.
    # second!
    DJ0 = Decimal(j0) / Decimal(24) / Decimal(3600.0)
    DJ1 = Decimal(j1) / Decimal(24) / Decimal(3600.0)
    Date = {"year":2018,"month":12,"day":29,"hour":19,"minute":16,"second":00,"ms":00}
    JD = DJ0 + DJ1
    MaximumJD = 10e9
    MinimumJD = -68569.5
    valid_jd = (JD < MaximumJD) & (JD > MinimumJD)
    if valid_jd==1:
        valid_text = "valid"
    else:
        valid_text = "invalid"
    #print("input Julian date(s)",JD,valid_text)
    # re-align to midnight
    if DJ0 >= DJ1:
        D1 = DJ0
        D2 = DJ1
    else:
        D1 = DJ1
        D2 = DJ0
    # separate day and fraction
    D2 = D2 - Decimal(0.5)
    F1  = D1 % 1
    F2  = D2 % 1
    F   = (D1 + D2) % 1
    if F < 0:
        F = F + 1;
    D = round(D1 - F1) + round(D2 - F2) + round(F1 + F2 - F)
    JD = int(round(D) + 1)
    L = int(JD + 68569)
    N = int(4 * L / 146097)
    L = ceil(L - (146097 * N + 3) / 4)
    I = int(4000 * (L + 1)/1461001)
    L = ceil(L - 1461 * I / 4 + 31)
    K = int(80 * L / 2447)
    ID = ceil(L - 2447 * K / 80)
    L = int(K / 11)
    IM = int(K + 2 - 12 * L)
    IY = int(100 * (N - 49) + I + L)
    FD = F
    Date["year"] = IY
    Date["month"]= IM
    Date["day"]  = ID
    H = int(F * 24)
    #print(F)
    LH= F * 24 - H
    #print(LH)
    M = int(LH * 60)
    LM = LH * 60 - M
    #print(LM)
    S = int (LM * 60)
    LS = LM * 60 - S
    #print(LS)
    MS = round(LS * 1000)
    # if MS == 1000:
    #     MS = 0
    #     S = S + 1
    # if S == 60:
    #     S = 0
    #     M = M + 1
    # if M == 60:
    #     M = 0
    #     H = H + 1
    #print(IY,IM,ID,H,LH,M,LM,S,LS,MS)
    Date["hour"] = H
    Date["minute"] = M
    Date["second"] = S
    Date["ms"] = MS
    return Date
