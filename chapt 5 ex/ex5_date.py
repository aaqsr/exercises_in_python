'''
This was fairly complicated for me
if anyone has a better way, send it to me
I used a pretty slow and inefficient method
'''

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
monthdays = {
    "January":0,
    "February":31, 
    "March":59, 
    "April":90, 
    "May":120, 
    "June":151, 
    "July":181, 
    "August":212, 
    "September":243, 
    "October":273, 
    "November":304, 
    "December":334
    }

month, day, year = input("Input date after 1900 in format <Full Month> <Day>, <Year>\n").replace(",", " ").split()
day = int(day)
year = int(year)
# month = 'June'; day = 28; year = 1920

# for leap year compensation
dyear = 1900
leapcomp = 0
while year > dyear:
    dyear += 1
    if ((dyear % 4 == 0 and not (dyear % 100 == 0 and dyear % 400 != 0))):
        leapcomp += 1

if (month == "January" and (dyear % 4 == 0 and not (dyear % 100 == 0 and dyear % 400 != 0))):
    leapcomp -= 1
if ((month == "February") and (dyear % 4 == 0 and not (dyear % 100 == 0 and dyear % 400 != 0))):
    leapcomp -= 1

# to calc total number of days
tdays = monthdays[month] + (day-1) + ((year-1900)*365) + leapcomp

# to determine which day that is
c = 0
for i in range(tdays):
    c += 1
    if (c>6):
        c = 0

# print
print(weekdays[c])

# issue with February 29, 1948 perhaps cause the date itself is leap
