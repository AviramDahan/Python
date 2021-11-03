import calendar

DATE = input("Please enter date dd/mm/yyyy: ")

yearM = int(DATE[6:10])
monthM = int(DATE[3:5])
dayM = int(DATE[0:2])

Day_Name = calendar.weekday(year=yearM, month=monthM, day=dayM)
Day_Name_Format = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print(Day_Name_Format[Day_Name])

