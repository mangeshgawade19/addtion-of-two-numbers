# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the sum
sum_result = add_numbers(num1, num2)

# Display the result
print("The sum of {} and {} is: {}".format(num1, num2, sum_result))
