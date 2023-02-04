# Chapter05: 9, 11, 16, 19, 26, 30, 35, 36, 53, 54, 55
# (Financial application: compute future tuition) Suppose that the tuition for a university
# is $10,000 this year and increases 5% every year. Write a program that
# computes the tuition in ten years and the total cost of four years’ worth of tuition
# starting ten years from now.

fees = 10000
interest = 1.05
total = 0
for i in range(1,15):
    fees += fees*interest
    if(i ==10):
        print("The cost of tuition in 10 years is $", fees)
    if(i>10):
        total= total+fees
