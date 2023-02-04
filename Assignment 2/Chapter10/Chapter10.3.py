# (Count occurrence of numbers) Write a program that reads some integers
# between 1 and 100 and counts the occurrences of each. Here is a sample run of
# the program:

numbers = input("ENTER numbers between 1 and 100 with a space")
nums = [int(s) for s in numbers.split()]
counted=[]
for no in nums:
    if no not in counted:
        c = nums.count(no)
        if c>1:
            print(str(no) + " Occurs "+ str(c) +" Times")
        else:
            print(str(no) + " Occurs "+ str(c) +" Times")
        counted.append(no)