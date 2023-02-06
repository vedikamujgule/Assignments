# (Current time) Listing 2.7, ShowCurrentTime.py, gives a program that displays the
# current time in GMT. Revise the program so that it prompts the user to enter the
# time zone in hours away from (offset to) GMT and displays the time in the specified
# time zone.
# import time

# timeZoneOffset = eval(input("Enter the time zone offset to GMT:"))
# currentTime = time.time()
# totalSeconds = int(currentTime)
# currentSecond = totalSeconds % 60
# totalMinutes = totalSeconds // 60
# currentMintute = totalMinutes % 60
# totalHours = totalMinutes // 60
# currentHour = totalHours % 24
# currentHour += timeZoneOffset
# print(currentHour, ":", currentMintute, ":", currentSecond)

#region 18 Solution
import time
enterTimeOffset = eval(input("Enter the time zone offset to GMT"))
currentTime = time.time()
sec_per_day = 60*60*24
sec_per_hour = 60*60

days_passed = currentTime / sec_per_day
sec_passed_today = currentTime % sec_per_day

hour_now = sec_passed_today // sec_per_hour

sec_passed_hour = sec_passed_today % sec_per_hour
minute_now = sec_passed_hour//60
sec_now = sec_passed_hour % 60

print("The current time is ",int(hour_now),":",int(minute_now),":",int(sec_now),sep="")

if hour_now >=0 and hour_now<=5:
    hour_now = 23 - (-enterTimeOffset) + 1 + hour_now  ## +1 to offset the hour when we transition from 23 to 00
else:
    hour_now += enterTimeOffset
print("The current time is ",int(hour_now),":",int(minute_now),":",int(sec_now),sep="")

#endregion