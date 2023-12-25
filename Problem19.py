#Counting Sundays

#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

class Day():
    def __init__(self) -> None:
        self.day : int = 1
        self.date = 1
        self.month = 1
        self.year = 1900
        self.leap = False

    def next(self):
        #If it's the last day of the week, set day = 0
        if self.day == 7:
            self.day = 0
        #Increment day
        self.day += 1
        
        #If it's the last day of the month, set date = 0 and increment month (if Dec, also set month = 0 and increment year)
        if self.month == 12:
            if self.date == 31:
                self.date = 0
                self.month = 1
                self.year += 1
                #Check for lear year
                if (self.year % 4 == 0) and ((not self.year % 100 == 0) or self.year % 400 == 0):
                    self.leap = True
                else:
                    self.leap = False
        if self.month in [1,3,5,7,8,10]:
            if self.date == 31:
                self.date = 0
                self.month += 1
        if self.month in [4,6,9,11]:
            if self.date == 30:
                self.date = 0
                self.month += 1
        if self.month == 2:
            if self.leap:
                if self.date == 29:
                    self.date = 0
                    self.month += 1
            if not self.leap:
                if self.date == 28:
                    self.date = 0
                    self.month += 1
        
        #Increment date
        self.date += 1


day = Day()
sundaysOnFirst = 0
while day.year < 1901:
    day.next()

if day.day == 7:
    if day.date== 1:
        sundaysOnFirst += 1

while day.year < 2001:
    day.next()
    if day.day == 7:
        if day.date == 1:
            sundaysOnFirst += 1

print(sundaysOnFirst)
        

