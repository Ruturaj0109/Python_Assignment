numbers = []

while True:
    user_input = input("Enter a number or 'q' to quit: ")

    if user_input.lower() == 'q':
        print("The even numbers you entered are:", numbers)
        break

    try:
        number = int(user_input)
        if number % 2 == 0:
            numbers.append(number)
    except ValueError:
        print("Invalid input, please enter a number or 'q'.")
