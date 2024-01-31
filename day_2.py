#this is a simple grade calculator
#the fact still remains that i am really tired, but then we have to stay committed
# we have to push each day, so yeahhh, here's to today
name = input("Hey there! Kindly provide your name: \n")
score = float(input("Thank you, now, please provide your score: \n"))


if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

"""F-string"""
print(f"The grade for the score {score} is {grade}.")


"""Modulus Operator"""
print("The grade for %s for the score %s is: %s" % (name, score, grade))


"""F-string"""
print(f"The grade for {name} for the score {score} is {grade}")