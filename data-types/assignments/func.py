def getParity(numbers):
    # Initialize two variables to count even and odd numbers
    even_count = 0
    odd_count = 0
    
    # Initialize an empty list for transformed numbers
    transformed_list = []
    
    # Loop through each number in the list
    for num in numbers:
        if num % 2 == 0:  # If the number is even
            even_count += 1  # Increase even count
            transformed_list.append(num * 2)  # Double the even number and add to the list
        else:  # If the number is odd
            odd_count += 1  # Increase odd count
            transformed_list.append(num * 3)  # Triple the odd number and add to the list
    
    # Print the results
    print("Even numbers:", even_count)
    print("Odd numbers:", odd_count)
    print("Transformed list:", transformed_list)

# Example usage with a list of numbers
L = [3, 2, 8, 9, 5]
getParity(L)
