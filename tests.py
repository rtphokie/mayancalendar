import unittest

from mayanCalendar import convert


class TestMayaDates(unittest.TestCase):
    def test_long_count_modern(self):
        lc, d = convert(2022, 6, 25)
        # 13.0.9.11.13
        # Tzolk'in Date: 6 B'en
        # Haab Date: 6 Sek
        # Lord of the Night: G8
        self.assertEqual([13, 0, 9, 11, 13], lc)
        self.assertEqual("6 B’en 6 Sek G8", d)

    # Test with glyphs on stella at the Quirigua site
    def test_Quirigua_stella_d(self):
        lc, d = convert(805, 7, 18)
        # 9.18.15.0.0
        # Tzolk'in Date: 3 Ajaw
        # Haab Date: 3 Yax
        # Lord of the Night: G9
        self.assertEqual([9, 18, 15, 0, 0], lc)
        self.assertEqual("3 Ajaw 3 Yax G9", d)

    def test_Quirigua_stella_e(self):
        # Jan 18, 771
        lc, d = convert(771, 1, 18)
        # 9.17.0.0.0
        # Tzolk'in Date: 13 Ajaw
        # Haab Date: 18 kumk'u
        # Lord of the Night: G9
        self.assertEqual([9, 17, 0, 0, 0], lc)
        self.assertEqual("13 Ajaw 18 Kumk’u G9", d)

    def test_Quirigua_stella_h(self):
        # May 3, 751
        lc, d = convert(751, 5, 3)
        # 9.16.0.0.0
        # Tzolk'in Date: 2 Ajaw
        # Haab Date: 13 Sek
        # Lord of the Night: G9
        self.assertEqual([9, 16, 0, 0, 0], lc)
        self.assertEqual("2 Ajaw 13 Sek G9", d)


if __name__ == '__main__':
    unittest.main()
