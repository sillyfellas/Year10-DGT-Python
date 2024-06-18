# Assignment 1 Fence Cost Calculator
# Author - Ecko Ordonez
# Version 2.0

# Greet user to the Fence Cost Calculator.
print("Welcome to the Fence Cost Calculator!")

# Ask user for all measurements (meters).

def calculate_cost():
    while True:
        length = float(input("Length of the area to be fenced in meters: "))
        width = float(input("Width of the area to be fenced in meters: "))
        cost_per_meter = float(input("Cost of fencing per meter: "))
        
        # This is the formula that should calculate the total cost.

        perimeter = 2 * (length + width)
        total_cost = perimeter * cost_per_meter
        
        print(f"The total cost of fencing is {total_cost} dollars.")

    # This line of code should give us an option to calculate again.
    
        cont = input("Do you want to calculate again? (yes/no): ")
        
        # (I had some help with this line of code thanks to co-pilot)

        if cont.lower() != "yes":
            break

calculate_cost()


    
        
