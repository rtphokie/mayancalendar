Converts dates in the Gregorian calendar dates in the Mayan calendar
including the 52-year cycle Calendar Round as well as the and the 5215-year
cycle long count from an epoch date of August 11, 3114 BCE.

Based on formulae from the [Smithsonian National Museum of the American Indian
exhibits on the Maya](https://maya.nmai.si.edu/).

# Usage
Convert a Gregorian date to a Mayan long count, and string describing the  
Haab, the Tzolk’in components of the calendar round.

* Syntax:
  * lc, d = convert(*year*, *month*, *day*)
* Returns:
  * array of long count components (baktun,katun,tun,uinal,k'in) 
  * string representation of the day and name the Haab and Tzolk’in months, and lord of night glyph number

```
>>> from mayanCalendar import convert
>>> lc, d = convert(2022, 6, 25)
>>> lc
[13,0,9,11,13]
>>> d
6 B’en 6 Sek G8
```