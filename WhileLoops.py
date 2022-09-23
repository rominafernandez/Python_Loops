## Exercise 24 - 3 while Loops

# Write a program that uses while loops to finish the tasks below, unknown length means
# that you define the length by yourself but don’t print it out:
# Searching for a specific number (e.g. 5) in an integer list of unknown length
# Multiplying all elements with each other of an integer list of unknown length (7 elements at least)
# Printing out the contents of a string list of unknown length elementwise

user_list = list(range(2,25,3))

# search for number 5
i = 0
while i < len(user_list):
    if user_list[i] == 5:
        print(f"The number 5 was found at index {i}.")
    i += 1

# multiply all elements
i = 1
result = user_list[0]
while i < len(user_list):
    result = result * user_list[i]
    i+=1
print(f"All elements multiplied by each other results in: {result}")

# printing a list
i = 0
while i < len(user_list):
    print(f"{i}. element: {user_list[i]}")
    i+=1
