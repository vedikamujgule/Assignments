# (Population projection) Rewrite Exercise 1.11 to prompt the user to enter the
# number of years and displays the population after that many years.

#  --From 1.11
# current population is 312032486
# One birth every 7 seconds
# One death every 13 seconds
# One new immigrant every 45 seconds

noOfYears = eval(input("Enter number of years: "))
currPopulation = 312032486
seconds = 365*24*60*60
newBirth = seconds/7
immigrants = seconds/45
death = seconds/13
res = int((currPopulation + (newBirth+immigrants-death)*noOfYears))
print("The population in 5 years is: " + str(res))