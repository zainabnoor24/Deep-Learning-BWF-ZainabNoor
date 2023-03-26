try:
    no = input("Give me a number: ")
    x = int(no)

    no2 = input("Give me another number: ")
    y = int(no2)
except ValueError:
    print("Sorry, I really needed a number.")
else:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}.")