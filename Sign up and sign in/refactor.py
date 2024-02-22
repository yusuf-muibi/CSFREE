print("Welcome to Tech-titans portal")
user_data = {}  # Dictionary to store user dat
print("type ctrl d or ctrl c to quit the program")

storage = '.database'
import json
import time

def signup():
    try:
        choice = input("Do you want to Sign Up or Sign In: ")

        if choice.lower() == 'sign up':
            user_info = {}  # Dictionary to store individual user's information
            choices = ["fullname", "username", "email"]

            # this senior boy is meant to only execute when choice is equal to sign up
            for usr_input in choices:
                user_info[usr_input] = input(f"Please Enter {usr_input}: ").strip()

            password = input("Create a password: ")
            user_info['password'] = password

            # Use the username as the key in the user_data dictionary
            user_data[user_info['username']] = user_info

            # open a file and write

            with open(storage, 'a') as db:
                # db.write(str(user_data))
                json.dump(user_data, db, indent=2)

            print(f"Successfully signed up {user_info['username']}")
        elif choice.lower() == 'sign in':
            signin()
        else:
            print('Invalid Input! Try Again')
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")

def signin():
    try:
        while True:
            signin_username = input("Kindly enter your username: ").strip()
            signin_password = input("Kindly enter your password: ")
            print("Processing...")
            time.sleep(2)

            with open(storage, "r") as db:
                user_data = json.load(db)
                
                if signin_username in user_data:
                    if user_data[signin_username]['password'] == signin_password:
                        print(f"Welcome {user_data[signin_username]['fullname']}")
                        break
                    else:
                        print("Invalid Password, please try again.")
                else:               
                    print("Invalid username, please try again")
                    time.sleep(2)            
                    print("Would you like to sign up now:")
                    choice = input("Yes/No: ")
                    if choice.lower() == 'yes':
                        signup()
                        break
                    else:
                        continue
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
#        time.sleep(2)
        quit()
try:
    signup()
except ValueError as ve:
    print(f'Error! ve')
