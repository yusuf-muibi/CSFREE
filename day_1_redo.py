#Write a Python function called find_largest_number that takes three numbers 
#as parameters and returns the largest among them. 
#Don't use any built-in Python functions like max().
#def find_largest_number(num1, num2, num3):
number = input("Kindly type in your numbers separated by a comma")
while True:
    numbers = [int(t) for t in number.split(',')]
    if len(numbers) != 3:
        print("Kindly input three digits")
    else:
        print(f"You typed in {numbers}")
        break
num1 = numbers[0]
num2 = numbers[1]
num3 = numbers[2]

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f"The order of the inputted number in descending order is {num1}, {num2}, {num3}")
    else:
        print(f"The order of the inputted number in descending order is {num1}, {num3}, {num2}")
elif  num2 > num1 and  num2 > num3:
    if  num1 > num3:
        print(f"The order of the inputted number in descending order is {num2}, {num1}, {num3}")
    else:
        print(f"The order of the inputted number in descending order is {num2}, {num3}, {num1}")
elif num3 > num1 and num3 > num2:
    if  num1>num2:
        print(f"The order of the inputted number in descending order is {num3}, {num1}, {num2}")
    else:
        print(f"The order of the inputted number in descending order is {num3}, {num2}, {num1}")
elif num1 == num2 == num3:
    print(f"All the numbers are equal i.e., {num1} ,{num2} & {num3}")
    

                  
    
    

# Test the function
# result = find_largest_number(15, 7, 22)
# print(result)  # It should print 22