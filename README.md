As seen on the [@MayaCalToday](https://twitter.com/MayaCalToday) Twitter account.

Converts dates in the Gregorian calendar dates in the Mayan calendar including the 52-year cycle Calendar Round as well
as the and the 5215-year cycle long count from an epoch date of August 11, 3114 BCE.

Based on formulae from
the [Smithsonian National Museum of the American Indian exhibits on the Maya](https://maya.nmai.si.edu/) which also has
a nice [interactive converter](https://maya.nmai.si.edu/calendar/maya-calendar-converter)

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

## Image Credits

All glyphs are in the public domain or Creative Commons licensed and available on English Wikipedia pages on
the [Mayan calendar](https://commons.wikimedia.org/wiki/Maya_calendar)
, [Haabʼ](https://en.wikipedia.org/wiki/Haab%CA%BC)
, [Mesoamerican Long Count calendar](https://en.wikipedia.org/wiki/Mesoamerican_Long_Count_calendar) pages.

* Tzolkin and Lord of the Night glyphs are provided by Wikipedia Commons contributoris Piquito Veloz and CJLL Wright
  respectively under the Creative Commons Attribution-Share Alike 3.0 license.
* Haab' month glyphs are in the public domain, from the 1905 book *An Introduction to the Study of the Maya Hieroglyphs*
  by Sylvanus Griswold Morley
* Long Count glyphs are provided by Wikipedia Commons contributor Catfan660