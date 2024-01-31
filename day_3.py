#Coding along with Sir Kelly 
#The question is to create a function that takes in a list as an input and return the result of the sum of the list

def list_sum(lst=None):
    sum=0
    for t in lst:
        sum = sum + t
    
    return sum

#test with predefined list

#total = list_sum([1,2,3,4,4,5,3,2,4,5,9,0])
#print(total)

#what if we want the user to type in the list?
user_input = input("Kindly type in the values of the list (separate each value using a comma): ")
#so now we have to use a for loop to iterate through the values given
#then split them using the specified character - ,
my_list = [float(x) for x in user_input.split(",")]
total = list_sum(my_list)

print(total)