#Write a program that allows users to sign up and then proceed to sign in
def login(email, password):   
    for user in users:
        if user["email"] == email and user["password"] == password:
            print("Login successful! Welcome,", user["First_name"])
            return True
    print("Incorrect email or password. Please try again.")
    return False
while True:
    print("Welcome to Techtitans portal")
    print("Kindly create an account if you are new or sign in if you already have an account")
    choice = input("Kindly type in 'Sign up' or 'Sign in'\n")

    users = []

    if choice.lower() == "sign up":
        first_name = input("Kindly enter your first name:\n")
        last_name = input("Kindly enter your last name\n")
        email = input("Kindly provide your email address:\n")
        password = input("Kindly type in a password of at least 8 characters\n")
        while True:
            if len(password) < 8:
                print("Password less than 8 characters, kindly try again")
                password = input("Please re-enter your password:\n")
            else:
                print(f"Hello {first_name}, your account has been successfully created")
                print("Your password has also been saved, kindly proceed to sign in")
                break
        users.append({"First_name": first_name, "Last_name": last_name, "Email": email, "Password": password})

        print("Would you like to sign in now?")
        sign_in = input("Type 'yes' to continue or any other key to exit\n").lower()
        
        if sign_in == "yes":
            email_input = input("Kindly type in the email address you registered with: \n")
            password_input = input("Kindly type in your password:")
            login(email_input, password_input)
        else:
            quit()


    elif choice.lower() == "sign in":
        email_input = input("Kindly type in the email address you registered with: \n")
        password_input = input("Kindly type in your password:")
        login(email_input, password_input)

    else:
        print("Invalid command. Please use 'Sign up' or 'Sign in'.")

    prompt_to_continue = input("Would you like to continue? (Press 'yes' to continue) \n").lower()
    if  prompt_to_continue != "yes":
        print("\nThank You for using our service!\n")
        break