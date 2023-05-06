# Generating a set of usernames
usernames = {'ruturaj_jadhav', 'jadhav_ruturaj', 'rutu_jadhav', 'jadhav_rutu', 'rutu_raj'}

# taking input
input_username = input("Please enter your username: ")

# Check if input username exists in set
if input_username in usernames:
    print(f"Welcome {input_username}!")
else:
    print(f"Sorry, {input_username} does not exist.")
