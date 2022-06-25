import datetime

from mayanCalendar.calendar_conversion import toLCD, to_tzolkin_date, to_haad_date, to_lord_number
from mayanCalendar.utils import dt_to_jd

def convert(y, m, d):
    jd = dt_to_jd(y, m, d)
    lc = toLCD(jd)
    td_num, td_name = to_tzolkin_date(jd)
    hd_num, hd_name = to_haad_date(jd)
    lord_num = to_lord_number(lc[3], lc[4])
    return lc, f"{td_num} {td_name} {hd_num} {hd_name} G{lord_num}"
