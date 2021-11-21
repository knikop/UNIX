import random
secret_num = random.randint(0,100)

print("Guess the SECRET NUMBER: ")
count = 1
while True:
    try:
        guess = int(input("Guess a number between 0 and 100: "))
    except ValueError():
        print("Only input a Number")
    if guess > secret_num:
        print("Less than")
        count += 1
    elif guess < secret_num:
        print("Greater than")
        count += 1
    elif guess == secret_num:
        print("Yay...You Guessed the SECRET NUMBER!!!")
        break
