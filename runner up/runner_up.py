#Given the participants score sheet for your University Sports Day, you are required to find the runner-up score. 
#You are given  scores. Store them in a list and find the score of the runner-up.
#Runner up score is the second highest number in the list
#pseudocode
#It receives input and uses the while loop as a seperator
#We are working with a list
#We will be using a sorted function 
#We will output the second number of the list

list = []

while True:
    user_input = input("Enter the scores of the participants and press 'done' when finished: ")
    if user_input.lower() == "done":
        break
    list.append(int(user_input))
    
list.sort()
runner_up = list[-2]
print("The runner up score is: ", runner_up)

