#30days challenge
#def add(x, y):
#    z = x+y
#    return x + y
#result = add(3, 5)
#print(result)  # Output: 8
#def my_function(parameter):
#    """This function does something."""
#    # Function body
#    return result
#def area_of_circle(radius):
#    area = 3.14 * radius ** 2
#    return area
#result = area_of_circle(7)
#print (result)
#def volume_of_sphere(radius):
#    return (4 / 3) * 3.14 * radius ** 3
#def calculate_interest(principal, rate, time):
#    return principal * rate * time
#def remove_duplicates(data):
#    return list(set(data))

# Write a Python function called calculate_total_cost that calculates the total cost of an order based on the 
#quantity of items ordered and their individual prices. The function should take two parameters:

# quantity: The quantity of items ordered (integer).
# price_per_item: The price per item (float).
# The function should calculate the total cost according to the following rules:

# If the quantity is less than or equal to 10, apply no discount.
# If the quantity is greater than 10 but less than or equal to 50, apply a 5% discount.
# If the quantity is greater than 50, apply a 10% discount.
# The function should return the calculated total cost.

# Write code to test your function with different quantities and prices per item.
import time
def calculate_total_cost(quantity, price_per_item):
    total_cost = 0
    if quantity <= 10:
        actual_price = quantity * price_per_item
        total_cost = (actual_price)
    elif quantity > 10 and quantity <= 50:
        discount = (quantity * price_per_item * 0.05)
        actual_price = quantity * price_per_item
        total_cost = (actual_price - discount)
    elif quantity > 50:
        discount = (quantity * price_per_item * 0.1)
        actual_price = quantity * price_per_item
        total_cost = (actual_price - discount)
    else:
        print("Error!")
        time.sleep(3)
        print("Exiting program!")
        quit()
    print(f"The actual price before discount is {actual_price}")
    print(f"The discounted price is:")
    return total_cost


print (calculate_total_cost(5, 20.3))
print (calculate_total_cost(15, 40.5))
print (calculate_total_cost(70, 50.7))

