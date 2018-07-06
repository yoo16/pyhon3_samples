import datetime as dt

class DateManager:
    @classmethod
    def setNumberForInterval(self, from_number, to_number):
        self.setFromNumber(from_number)
        self.setToNumber(to_number)
        return self

    @classmethod
    def setFromNumber(self, number):
        self.from_number = number
        self.from_datetime = self.numberToDatetime(number)
        return self

    @classmethod
    def setToNumber(self, number):
        self.to_number = number
        self.to_datetime = self.numberToDatetime(number)
        return self

    @classmethod
    def numberToDatetime(self, number):
        year = self.numberToYear(number)
        month = self.numberToMonth(number)
        day = self.numberToDay(number)
        hour = self.numberToHour(number)
        minute = self.numberToMinute(number)
        datetime = dt.datetime(year, month, day, hour, minute)
        return datetime

    @classmethod
    def numberToYear(self, number):
        return int(number[0:4])

    @classmethod
    def numberToMonth(self, number):
        return int(number[4:6])

    @classmethod
    def numberToDay(self, number):
        return int(number[6:8])

    @classmethod
    def numberToHour(self, number):
        return int(number[8:10])

    @classmethod
    def numberToMinute(self, number):
        return int(number[10:12])