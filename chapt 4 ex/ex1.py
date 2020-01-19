tm = input("How much money do you have?\n$")
day = input("What day of the month is it today?\n")
# monthday = input("How many days in the month?\n")
month = input("What month is it?\n")
# user input 

monthday = {'Jan':31, "Feb":28, 'Mar':31, 'Apr':30, 'May':31, 'Jun':30, 'Jul':31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}

mpd = float(tm)/(int(monthday[month]) - int(day)) # simple calculation
print("You can spend ${0:0.2f} today".format(mpd)) # simple print