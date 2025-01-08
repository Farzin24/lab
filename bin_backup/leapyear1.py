import calendar
cyear=2024
fyear=int(input("enter the final year:"))
lyear=[ ]
for year in range(cyear,fyear+1):
   if calendar.isleap(year):
       lyear.append(year)
print("leap years is:")
for year in lyear:
   print(year)

