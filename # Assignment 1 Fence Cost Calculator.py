# Assignment 1 Fence Cost Calculator
# Author - Ecko Ordonez
# Version 1.0

# Greet user to the Fence Cost Calculator 
print("Welcome to the Fence Cost Calculator!")

# Ask user for all measurements (meters)
print("please enter all the following measurments in meters.")

error = "Please enter a number that is more than zero\n"
if True:

    try: 
        
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
    
    
    perimeter = width * length
    total = cost_per_meter * perimeter
    
    print(f"Perimeter is {perimeter} ")
    print(f"Total cost is {total} ")

    float (input("Would you calculate again?(if you entered a number that is zero or bellow)"))

    
        
