def multiple(x, y):
    return (y % x) == 0

print("--Python Program--")
y = int(input("Enter the multiple: "))
x = int(input("Enter a number: "))
print("true" if multiple(x, y) else "false")