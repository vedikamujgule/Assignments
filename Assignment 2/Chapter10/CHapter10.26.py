# (Merge two sorted lists) Write the following function that merges two sorted lists
# into a new sorted list:
# def merge(list1, list2):
# Implement the function in a way that takes len(list1) + len(list2) comparisons.
# Write a test program that prompts the user to enter two sorted lists and
# displays the merged list. Here is a sample run:


def merge(list1, list2):
    res = []
    c1 = 0
    c2 = 0
    while c1 < len(list1) and c2 < len(list2):
        m1 = list1[c1]
        m2 = list2[c2]
        if m1 < m2:
            res.append(m1)
            c1 += 1
        else:
            res.append(m2)
            c2 += 1
            
    while c1 < len(list1):
        res.append(list1[c1])
        c1 += 1

    while c2 < len(list2):
        res.append(list2[c2])
        c2 += 1
    return res
    print(res)

list1 = [int(x) for x in input("Enter sorted list1 : ").split()]
list2 = [int(x) for x in input("Enter sorted list2: ").split()]
res = merge(list1, list2)
print(res)