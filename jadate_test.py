import datetime
from jadate import *
import unittest

class TestJaDate(unittest.TestCase):
    def test8(self):
        d = JaDate.fromStr('20140123')
        self.assertEqual(d.year, 2014)
        self.assertEqual(d.month, 1)
        self.assertEqual(d.day, 23)

    def test4ThisYear(self):
        d1 = datetime.date.today() + datetime.timedelta(days=1)
        s = "{:02}{:02}".format(d1.month, d1.day)
        d2 = JaDate.fromStr(s)
        self.assertEqual(d1.year, d2.year)
        self.assertEqual(d1.month, d2.month)
        self.assertEqual(d2.day, d2.day)

    def test4NextYear(self):
        today = datetime.date.today()
        d1 = today - datetime.timedelta(days=1)
        if today.year == d1.year:
            s = "{:02}{:02}".format(d1.month, d1.day)
            d2 = JaDate.fromStr(s)
            self.assertEqual(d2.year, today.year + 1)
            self.assertEqual(d2.month, d1.month)
            self.assertEqual(d2.day, d1.day)
