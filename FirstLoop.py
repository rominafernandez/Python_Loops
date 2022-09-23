## Exercise 23 - Your first Loops

# All following loops should run at least over a range from 0 to 21
# Write one loop that sums up all numbers in the setted range
# Write another loop that sums up only the even numbers in the setted range
# Write a third loop that generates a list that contains the values of the range in reverse order
# Print out all three results

# Summing up
sum = 0
for i in range(22):
    sum = sum + i

# Summing up even numbers
sum_even = 0
for i in range(22):
    if i % 2 == 0:
        sum_even = sum_even + i

# Reverse order
result_list = list(range(22))
for i in range(22):
    result_list[len(result_list)-(i+1)] = i


print(f"Sum: {sum}")
print(f"Sum even: {sum_even}")
print(f"Reverse order: {result_list}")
