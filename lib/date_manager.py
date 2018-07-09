import datetime as dt

class DateManager:
    from_number = ''
    to_number = ''
    from_datetime = ''
    to_datetime = ''

    def __init__(self):
        return

    def setNumberForInterval(self, from_number, to_number):
        self.setFromNumber(from_number)
        self.setToNumber(to_number)
        return self

    def setFromNumber(self, number):
        self.from_number = number
        self.from_datetime = self.numberToDatetime(number)
        return self

    def setToNumber(self, number):
        self.to_number = number
        self.to_datetime = self.numberToDatetime(number)
        return self

    def numberToDatetime(self, number):
        year = self.numberToYear(number)
        month = self.numberToMonth(number)
        day = self.numberToDay(number)
        hour = self.numberToHour(number)
        minute = self.numberToMinute(number)
        datetime = dt.datetime(year, month, day, hour, minute)
        return datetime

    def numberToYear(self, number):
        return int(number[0:4])

    def numberToMonth(self, number):
        return int(number[4:6])

    def numberToDay(self, number):
        return int(number[6:8])

    def numberToHour(self, number):
        return int(number[8:10])

    def numberToMinute(self, number):
        return int(number[10:12])
