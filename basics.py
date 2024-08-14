### TASK 3- Assignment2

import json


def load_user():
    try:
        with open("database.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_user(user):
    with open("./database.json", "w") as file:
        json.dump(user, file)


def sign_up():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    mobile_number = input("Enter your mobile number: ")

    user_data = load_user()

    if username in user_data:
        print("Username already exists. Please choose a different username.")
        return

    user_data[username] = {"password": password, "mobile_number": mobile_number}

    save_user(user_data)
    print("Sign up successful!\n")


def sign_in():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user = load_user()

    if username in user and user[username]["password"] == password:
        print("Sign in successful!")
        print(
            f"Welcome to the device!\n Your phone number is: {user[username]['mobile_number']}\n"
        )
    else:
        print("Sign In Failed! Invalid username or password.\n")


def main():
    while True:
        print("AVAILABLE OPTIONS:")
        print("1. Sign up")
        print("2. Sign in")
        print("3. Exit")

        choice = input("Enter choice [1,2,3]: ")

        if choice == "1":
            sign_up()
        elif choice == "2":
            sign_in()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try Again!\n")


main()


# # Exceptions, error handling

# try:
#     # Attempt to access a file that doesn't exist
#     with open('nonexistent_file.txt', 'r') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("The file does not exist.")
#     # create and open file
#     with open('nonexistent_file.txt', 'w') as file:
#         file.write("This is a placeholder for the nonexistent file.")

# # Attempt to divide by zero
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
#     result = None


# # start infinite while loop, get random numbers in numerator and denominator, calculate total number of crashes and terminate the program if total crashes equals to 5

# import random
# total_crashes = 0
# while True:
#     try:
#         numerator = random.randint(0, 10)
#         denominator = random.randint(0, 10)
#         result = numerator / denominator
#         print(f"Result: {numerator}/{denominator} = {result}")
#     except:
#         total_crashes += 1
#         print(f"Crashed! {numerator}/{denominator}")
#         if total_crashes == 5:
#             print("Total crashes reached 5. Terminating the program.")
#             break


## file handling
# def write_note():
#     with open("database.txt", "a") as file:
#         note = input("Write a note: ")
#         file.write(note + "\n")

# def read_notes():
#     try:
#         with open("database.txt", "r") as file:
#             notes = file.read()
#             if notes:
#                 print("Notes:\n")
#                 print(notes)
#             else:
#                 print("No notes found.")
#     except FileNotFoundError:
#         print("No notes.")

# def main():
#     while True:
#         print("1. Write note")
#         print("2. Read note")
#         print("3. Exit")

#         choice = input("Enter choice: ")

#         if choice == "1":
#             write_note()
#         elif choice == "2":
#             read_notes()
#         elif choice == "3":
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice.")

# main()


# def sign_up():
#     username = input("Enter a username: ")
#     password = input("Enter a password: ")
#     mobile_number = input("Enter your mobile number: ")

#     with open("user_database.txt", "a") as file:
#         file.write(f"{username},{password},{mobile_number}\n")
#     print("Sign up successful!")

# def sign_in():
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")

#     try:
#         with open("user_database.txt", "r") as file:
#             users = file.readlines()

#         for user in users:
#             stored_username, stored_password, _ = user.strip().split(",")
#             if username == stored_username and password == stored_password:
#                 print('*'*50)
#                 print("Sign in successful!")
#                 print('*'*50)
#                 return "Success"
#         print("Sign in failed! Invalid username or password.")
#     except FileNotFoundError:
#         print("No users found. Please sign up first.")

# def main():
#     while True:
#         print("1. Sign up")
#         print("2. Sign in")
#         print("3. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             sign_up()
#         elif choice == "2":
#             sign_in()
#         elif choice == "3":
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice. Please choose again.")

# main()
