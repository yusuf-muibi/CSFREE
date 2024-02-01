#This is the fourth day
#Writing a program that finds the factorial of a number and return the factorial
#use a while loop to check if the input is a positive number

def factorial(number):
    factorial_result = 1
    for i in range(1, number + 1):
        factorial_result *= i
    return factorial_result

while True:
    user_input = input("Enter a positive number: \n")
    
    if user_input.lstrip("-").isdigit():
        number = int(user_input)
        if number >= 0:
            answer = factorial(number)
            print(f"The factorial of {number} is factorial{answer}")
            break
        else:
            print("Please enter a non - negative integer.")
    else:
        print("Please enter an integer.")