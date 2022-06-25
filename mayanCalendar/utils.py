import math

def inty(x):
    # rounds positive numbers down, negative numbers up
    if x > 0:
        return math.floor(x)
    else:
        return math.ceil(x)

def dt_to_jd(y,m,d):
    if 1 <= m <= 2:
        y -= 1.0
        m += 12.0
    B = 0.0;
    if ((y > 1582.0) or ((y == 1582.0) and (m > 10.0)) or ((y == 1582.0) and (m == 10.0) and (d > 15.0))):
        A = inty(y / 100.0);
        B = 2.0 - A + inty(A / 4.0)
    jd = inty(365.25 * (y + 4716.0)) + inty(30.600100000000001 * (m + 1.0)) + d + B - 1524.5
    return jd

