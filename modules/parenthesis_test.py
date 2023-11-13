import re

def remove_parentheses(input_string):
    # Use regular expression to remove everything inside parentheses
    pattern = r"\([^)]*\)"
    result = re.sub(pattern, "", input_string)
    return result

# Example usage
input_string = "This is a (sample) string (with multiple) sets of parentheses."
output_string = remove_parentheses(input_string)
print("Original String:", input_string)
print("String after removing parentheses:", output_string)
