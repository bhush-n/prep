# Slice operator is used to extract a portion of a sequence (like a list, tuple, or string) 
# by specifying a start index, an end index, and an optional step.

# Syntax: sequence[start:stop:step]
# start: The index where the slice starts (inclusive). Default is 0.
# stop: The index where the slice ends (exclusive). Default is the length of the sequence
# step: The step size or the interval between indices. Default is 1.

# Example with a list
x = [1, 2, 3, 4, 5]

sliced = x[1:4:2]  # This will extract elements from index 1 to index 3 with a step of 2

print(sliced) # Output: [2, 4]

# Example with a string
s = "Hello, World!"

sliced_string = s[0:5]  # This will extract the first 5 characters

print(sliced_string) # Output: Hello