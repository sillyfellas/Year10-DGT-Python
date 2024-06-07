# Assignment 1 Fence Cost Calculator
# Author - Ecko Ordonez
# Version 1.0

# Greet user to the Fence Cost Calculator.
print("Welcome to the Fence Cost Calculator!")

# Ask user for all measurements (meters).
print("please enter all the following measurments in meters.")

# Making a variable "error" equal to "please enter a number that is more than" allow us to display
# "please enter a number higher than zero".

error = "Please enter a number that is more than zero\n"
while True:

    try: # This whole function allows the user to input their measurements.
        # If they insert a zero, it should ask them to insert a number higher than zero. 
        
        width = float(input("Width:"))
        length = float (input("Length:"))
        cost_per_meter = float(input("Cost per meter:"))

        if width > 0:
            done = True
        if length > 0:
            done = True
        if cost_per_meter > 0:
            done = True
        else:
            print(error)

    except ValueError:
        print(error)
    



 # This piece of code should show us all the results of our measurements.
 # It should also allow us to calculate again. 


    perimeter = width * length
    total = cost_per_meter * perimeter
    
    print(f"Perimeter is {perimeter} ")
    print(f"Total cost is {total} ")

    input = str(input("Would you calculate again?"))
    if input == "yes":
        continue
    elif input == "no":
        break



    
        
