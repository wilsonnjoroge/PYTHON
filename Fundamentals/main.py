def check_if_zero(num):
    if num == 0:
        return "The number cannot be zero."
    return None  # Return None if the number is not zero

def add_numbers(num1, num2):
    # Check if either number is zero
    zero_check = check_if_zero(num1)
    if zero_check:
        return zero_check  # Return the message if num1 is zero

    zero_check = check_if_zero(num2)
    if zero_check:
        return zero_check  # Return the message if num2 is zero

    result = num1 + num2
    return "The result is: " + str(result)

# Test the function
print(add_numbers(2, 2))  # Should print the result
print(add_numbers(0, 2))  # Should print the error message
print(add_numbers(2, 0))  # Should print the error message
