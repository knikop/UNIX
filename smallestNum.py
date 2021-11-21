#Find the smallest number in the list
list = [10, 34, 56, 77, 88, 54, 52, 3, 2, 3, 4, 98, 5, 6, 8, 15, 17, 23, 31, 1]
list.sort()
print("Smallest Number is: ", *list[:1])