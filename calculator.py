# This is an array to store the numbers to be used in the calculation
# it also stores the operator function.
nums = []


# Get input function reads the user's input and inserts it into an array:
def get_input():
    first_number = input("Enter a first number: ")
    math_func = input("What do you want to do? +, -, *, / :")
    second_number = input("Enter a second number: ")
    # This line of code inserts the 'first_number' variable into the first
    # position of the array nums. It can be accessed via: nums[0]
    nums.insert(0, first_number)
    # As mentioned above, this also inserts 'second_number' into the second
    # position in the array nums. It can be accessed via: nums[1]
    nums.insert(1, second_number)
    # This inserts the value of the operator into the array nums.
    # This inserts the value of the operator into the array nums.
    nums.insert(2, math_func)
    return nums


# Add function returns the sum of the first number and second number:
def add_func(a, b):
    return int(a) + int(b)


# Subtract function subtracts the second number from the first number:
def subtract_func(a, b):
    return int(a) - int(b)


# Multiply function produces the product of the two numbers:
def multiply_func(a, b):
    return int(a) * int(b)


# Divide function divides the first number by the second number:
def divide_func(a, b):
    return int(a) / int(b)


# Equal function prints out the results to the console
def equal_func(res):
    print("The result is: " + str(res))


# Main function:
def main():
    # Here we call the get_input() function:
    get_input()

    # This 'if... then... else...' statement handles the decision of what
    # to do with the two numbers. i.e. based on the function the user wants
    # to perform. Either Add '+', Subtract '-', Multiply '*' or Divide '/':
    if nums[2] == "+":
        # If addition is chosen during the get_input() function this code will be run:
        res = add_func(nums[0], nums[1])
    elif nums[2] == "-":
        # If subtraction is chosen during the get_input() function this code will be run:
        res = subtract_func(nums[0], nums[1])
    elif nums[2] == "*":
        # If multiplication is chosen during the get_input() function this code will be run:
        res = multiply_func(nums[0], nums[1])
    elif nums[2] == "/":
        # If division is chosen during the get_input() function this code will be run:
        res = divide_func(nums[0], nums[1])
    # This then prints out the value assigned to the 'res' variable from within the 'if then else' statement above.
    equal_func(res)


# Calls the main function to be run:
if __name__ == '__main__':
    main()
