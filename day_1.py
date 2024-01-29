#So, What do we start with?
#We'll be starting with a refresher on Loops
#First will be to print odd numbers from 1 to 21
print("The odd numbers from 1-21 are:")
for t in range(1, 21):
    if t % 2 != 0:
        print(t)


#okay, second will be to use the .format print type, tho i prefer sing % for my printing
#so, here we will be printing floating point into 2 decimal places
#this is just to know how to use the decimal place thing really
#i also added other print types and how to use the 2 decimal places
my_number = float(input("Kindly type in the float you'd like to convert to 2 decimal places\n"))
print("Round to 2 decimals: {:.2f}".format(my_number))
print("Round to 2 decimals: %.2f" % (my_number))
print(f"Round to 2 decimals: {my_number:.2f}")

#okay, that worked fine, so what's next
#so next, we calculate simple interest, or is it compound?
#anyway,the idea is that the user provides their principal investment and their interest rate
#and then we calculate the Interest over 10 years
#let's get started
final_interest = 0
print("Hey there, this is the Interest calculator")
principal = float(input("Kindly provide the amount you would like to invest\n"))
rate = float(input("Fantastic, now kindly provide your desired interest rate. (NB:no need for percentage)\n"))
interest_rate = (rate*.01)
#the above is to convert the percentage to decimal
print("Your Principal is N %s, and your interest rate is %s" % (principal, rate))
for t in range(1, 11):
#the below calculates the interest
    interest = (principal + (principal*interest_rate))
#%.2f converts the answer to 2 decimal place
print("Your investment after 10 years is: #%.2f" % (interest))
