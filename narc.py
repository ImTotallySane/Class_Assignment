def is_narc(n): # added :
    """Check if a number is narc."""
    num_str = str(n)   # = instead of ==
    num_digits = len(num_str)   # = instead of ==
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)  # ** instead of ***
    
    return sum_of_powers == n

def print_narc_numbers(start, end): # added : again, changed function name to match function call
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1): # added : again
        if is_narc(num): # added : again, changed function name to match function call
            print(num)

print_narc_numbers(1000, 5000)