class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour  
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
     
        total_seconds = self.__second + other.__second
        total_minutes = self.__minute + other.__minute + total_seconds // 60
        total_hours = self.__hour + other.__hour + total_minutes // 60

       
        seconds = total_seconds % 60
        minutes = total_minutes % 60
        hours = total_hours % 24  
        return Time(hours, minutes, seconds)

    def display(self):
        return f"{self.__hour:02}:{self.__minute:02}:{self.__second:02}"


hour1 = int(input("Enter hours for the first time: "))
minute1 = int(input("Enter minutes for the first time: "))
second1 = int(input("Enter seconds for the first time: "))
time1 = Time(hour1, minute1, second1)


hour2 = int(input("Enter hours for the second time: "))
minute2 = int(input("Enter minutes for the second time: "))
second2 = int(input("Enter seconds for the second time: "))
time2 = Time(hour2, minute2, second2)


sum_time = time1 + time2


print("First Time:", time1.display())
print("Second Time:", time2.display())
print("Sum of Times:", sum_time.display())
 
