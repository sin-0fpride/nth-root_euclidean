# Function to find the nth root of a number using binary search
def nth_root(number, n):
    # Handle edge cases for invalid inputs
    if number == 0:  # If number is 0, nth root is 0
        return 0
    if n == 0:  # If n is 0, nth root is undefined
        raise ValueError("n cannot be 0")
    
    # Check if number is negative and if n allows for real roots
    is_negative = number < 0
    if is_negative and n % 2 == 0:  # Even roots of negative numbers are not real
        raise ValueError("Cannot compute even root of a negative number")
    number = abs(number)  # Work with absolute value for simplicity
    
    # Set up binary search range
    low = 0
    high = max(1, number)  # Upper bound: number or 1 (for numbers < 1)
    precision = 0.0001  # Define precision for approximation
    
    # Binary search loop to approximate nth root
    while high - low > precision:  # Continue until close enough
        mid = (low + high) / 2  # Find midpoint
        power = mid ** n  # Compute mid raised to nth power
        if power > number:  # If too high, reduce upper bound
            high = mid
        else:  # If too low, increase lower bound
            low = mid
    
    result = low  # Final approximation of nth root
    if is_negative:  # Adjust sign for negative input (only for odd n)
        result = -result
    return result
print(nth_root(16, 4))  # Should print ~2 (4th root of 16)


