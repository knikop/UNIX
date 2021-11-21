even_count = 0
odd_count = 0
even_sum = 0
odd_sum = 0
total = 0

while True:
    num = int(input("Input an int(100 stops): "))
    if num == 100:
        break
    if num < 1:
        continue
    if num % 2 == 0:
        even_count += 1
        even_sum += num
    else:
        odd_count += 1
        odd_sum += num
    total += 1

print("")
print("Sum of odds:", odd_sum)
print("Sum of evens:", even_sum)
print("Even count:", even_count)
print("Odd count:", odd_count)
print("Total positive int count:", total)