print("Enter the Value of number: ", end="")
number = int(input())
print("Enter " +str(number)+ " Numbers: ", end="")
numbers = []
i = 0
while i < number:
    numbers.append(int(input()))
    i = i+1

sum = 0
i = 0
while i < number:
    sum = sum+numbers[i]
    i = i+1

avg = sum/number
print("\nAverage = ", avg)
total = sum
print("\nTotal = ", total)