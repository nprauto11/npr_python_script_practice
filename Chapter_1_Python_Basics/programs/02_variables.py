# variables.py
# This script demonstrates the use of variables in Python and accepts user input.

# Existing variable assignments with default values
default_string = "SRE Engineer"    # Default username (string example)
default_integer = 10               # Default count (integer example)
default_float = 3.14               # Default ratio (float example)

# Print the default values
print("Default Username:", default_string)
print("Default Count:", default_integer)
print("Default Ratio:", default_float)

# Accept user input for username
user_string = input("Enter a username (or press Enter to keep default): ") or default_string

# Accept user input for count and convert to an integer
try:
    user_integer = int(input("Enter a count (or press Enter to keep default): ") or default_integer)
except ValueError:
    user_integer = default_integer  # Keep default if conversion fails

# Accept user input for ratio and convert to a float
try:
    user_float = float(input("Enter a ratio (or press Enter to keep default): ") or default_float)
except ValueError:
    user_float = default_float  # Keep default if conversion fails

# Print the final values of the variables
print("\nFinal Username:", user_string)
print("Final Count:", user_integer)
print("Final Ratio:", user_float)

# Explanation:
# - The script starts by defining default variable values for a string, an integer, and a float.
# - It prints these default values to the console.
# - It then prompts the user to enter a new value for the username, allowing them to keep the default by pressing Enter.
# - For count and ratio, it attempts to convert user input to an integer or float, respectively, 
#   and retains the default value if the input is invalid.
# - Finally, it prints the final values of the variables.
