import math
from mayanCalendar.utils import dt_to_jd


def to_long_count(jdn):
    # based on algorithm developed by Smithsonian National Museum of the American Indian
    longCount = [None, None, None, None, None]
    days = round(jdn - 584282.5)  # epoch of August 11, 3114 BCE.

    durations = []

    longCount[0] = math.floor(days / 144000)
    days %= 144000

    longCount[1] = math.floor(days / 7200)
    days %= 7200

    longCount[2] = math.floor(days / 360)
    days %= 360

    longCount[3] = math.floor(days / 20)

    longCount[4] = math.floor(days % 20)

    return longCount


def to_tzolkin_date(jdn):
    tzolkin_names = ['Imix’', 'Ik’', 'Ak’bal', 'K’an', 'Chikchan', 'Kimi', 'Manik’', 'Lamat', 'Muluk', 'Ok', 'Chuwen',
                    'Eb', 'B’en', 'Hix', 'Men', 'K’ib’', 'Kaban', 'Etz’nab’', 'Kawak', 'Ajaw']  # tzolk'in
    longCount = round(jdn - 584282.5);
    cnt = (((longCount + 3) % 13) + 1)
    day = ((longCount + 19) % 20)
    return cnt, day, tzolkin_names[day]


def to_haad_date(jdn):
    haad_names = ['Pop', 'Wo’', 'Sip', 'Sotz’', 'Sek', 'Xul', 'Yaxk’in', 'Mol', 'Ch’en', 'Yax', 'Sak’', 'Keh', 'Mak',
                   'K’ank’in', 'Muwan', 'Pax', 'K’ayab', 'Kumk’u', 'Wayeb’']  # haab'
    longCount = round(jdn - 584282.5)
    dayOfHaab = (longCount - 17) % 365
    day = round(dayOfHaab % 20)
    month = round(math.floor(dayOfHaab / 20))
    return day, month, haad_names[month]


def to_lord_number(x, y):
    return ((20 * x + y + 8) % 9 + 1)


def convert(y, m, d):
    jd = dt_to_jd(y, m, d)
    lc = to_long_count(jd)
    td_num, td_day, td_name = to_tzolkin_date(jd)
    hd_num, hd_day, hd_name = to_haad_date(jd)
    lord_num = to_lord_number(lc[3], lc[4])
    return lc, [td_num, td_day+1, hd_num, hd_day, lord_num], f"{td_num} {td_name} {hd_num} {hd_name} G{lord_num}"