# Chapter01: 11, 18, 21

# (Population projection) The US Census Bureau projects population based on the
# following assumptions:
# One birth every 7 seconds
# One death every 13 seconds
# One new immigrant every 45 seconds
# Write a program to display the population for each of the next five years. Assume the
# current population is 312032486 and one year has 365 days. Hint: in Python, you
# can use integer division operator // to perform division. The result is an integer. For
# example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5).

currPopulation = 312032486
seconds = 365*24*60*60*5
newBirth = seconds//7
immigrants = seconds//45
death = seconds//13
print(int(currPopulation+newBirth+immigrants-death))


