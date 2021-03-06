import datetime

class JaDate(datetime.date):
    """
    文字列の様式
    (1) ８つの数字
        最初の４桁が西暦の年、次の２桁が月、最後の２桁が日
    (2) ４つの数字
        最初の２桁が月、あとの２桁が日
        年は、本日から一年後一日前までの期間のもの
    (3) ３つの数字
        最初の１桁が月、あとの２桁が日
    """
    @classmethod
    def from_str(cls, s, today):
        if len(s) == 8:
            return JaDate(int(s[:4]), int(s[4:6]), int(s[6:]))
        elif len(s) == 4:
            return JaDate._from_month_and_day(int(s[:2]), int(s[2:]), today)
        elif len(s) == 3:
            return JaDate._from_month_and_day(int(s[:1]), int(s[1:]), today)
        else:
            raise ValueError('invalid length str given to fromStr')

    @staticmethod
    def _from_month_and_day(m, d, today):
        date = JaDate(today.year, m, d)
        if today <= date:
            return date
        else:
            return JaDate(today.year + 1, m, d)

    WEEKDAYS = ("月", "火", "水", "木", "金", "土", "日")
    def ja_weekday(self):
        return JaDate.WEEKDAYS[self.weekday()]

    def format(self, format):
        return format.format(year=self.year, month=self.month, day=self.day,
                             weekday=self.ja_weekday())
