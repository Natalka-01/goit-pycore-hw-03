
import random

def get_numbers_ticket(min, max, quantity):
    if min < 1: #Checking the parameter "min" greater that 1
        print("The number need to be greater that 1.")
    elif max > 1000: #Checking the parameter "max" greater that 1000
        print("This number need to not greater than 1000.")
    elif quantity > (max - min): #Checking if the quantity of numbers to generate is greater than the available range, and printing error message
        print("The quantity is greater then numbers of the range")
    else:
        numbers = []
        while quantity > 0:
            #Generating random number between the range and checking if this nomber exist in the list, if yes start loop again.
            item = random.randrange(min, max+1)
            if item in numbers:
                continue
            else: #If the number is not in the list, add it
                numbers.append(item)
                quantity -=1
        return numbers
    
result = get_numbers_ticket(1,100,6)
result.sort()
print(result)

    