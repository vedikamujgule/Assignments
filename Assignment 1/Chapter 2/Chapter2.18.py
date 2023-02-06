# (Current time) Listing 2.7, ShowCurrentTime.py, gives a program that displays the
# current time in GMT. Revise the program so that it prompts the user to enter the
# time zone in hours away from (offset to) GMT and displays the time in the specified
# time zone.
# import time

import time
enterTimeOffset = eval(input("Enter the time zone offset to GMT: "))
currentTime = time.time()
secondsPerDay = 60*60*24
secondsPerHour = 60*60

days_passed = currentTime / secondsPerDay
sec_passed_today = currentTime % secondsPerDay

hour_latest = sec_passed_today // secondsPerHour

sec_passed_hour = sec_passed_today % secondsPerHour
minute_latest = sec_passed_hour//60
sec_latest = sec_passed_hour % 60

if hour_latest >=0 and hour_latest<=5:
    hour_latest = 23 - (-enterTimeOffset) + 1 + hour_latest
else:
    hour_latest += enterTimeOffset
print("The current time is: ",int(hour_latest),":",int(minute_latest),":",int(sec_latest),sep="")
