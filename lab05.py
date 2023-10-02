"""
Author:         Folu Taiwo
Date:           9/26/23
Assignment:     Lab 05
Course:         CPSC1051
Lab Section:    003

CODE DESCRIPTION:

"""

print("Welcome to the Magic Square!")
#Ask user for input 
print('Enter in the magic square size you would like:')
size = int(input())
#Input validation
while size <= 0:
    #Check if the number is greater than zero
    print('Please enter in a number that is greater than 0')
    print('Enter in the magic square size you would like:')
    size = int(input())

total_square_spaces = size ** 2
num_total = 0
for num in range(total_square_spaces+1):
    num_total += num

magic_number = num_total / size
print(f'The magic number for size {size} is {int(magic_number)}.')

#Enter the magic square as a list of numbers
print('Enter in the values separated by spaces: ')
values = input().strip()
values_list = values.split() # 1 2 3 4 5 -> ["1", "2", "3", "4", "5"]

#Initialize a 2D list
init_list = [['' for i in range(size)] for j in range(size)]

#Convert each item to int type and store in the 2D list
for i in range(size):
    for j in range(size):
        init_list[i][j] = values_list[i * size + j]

print('Your square:')
for i in range(size):
    for j in range(size):
        print(f"{init_list[i][j]}" , end= ' ') 
    print('\n')

    
# Generate the expected list with numbers 1 to n^2
expected = [i for i in range(1, size**2 + 1)]
    
# Flatten the 2D list into a 1D list
flattened = values_list

    
# Sort both lists
expected = expected.sort()
flattened = flattened.sort()
    
# Check if the sorted lists are equal
if flattened != expected:
    print(f'The input cannot be a magic square! There must be one of each value from 1 to {size**2}.')

#Check rows
for i in range(size):
    for j in range(size):
        if init_list[j][i] != init_list[2][i]:
            print(f'Row {i} does not work! These are the values in row {i}: ', end = '')   
            print(f'{init_list[j][i]}')
    
# Check columns
for j in range(size):
    if init_list[j][i] != init_list[j][2]:
        print(f'Column {i} does not work! These are the values in column {i}: ', end = '')
        print(f'{init_list[j][i]}')

#Check upper to lower diagonal
for i in range(size):
    if init_list[i][i] != init_list[0][0]:
        print('Diagonal 1 does not work! ')
        print('These are the values in diagonal 1: ', end = '')
        print(f'{init_list[i][i]}')

#Check lower to upper diagonal
    if init_list[i][(size - 1) - i] != init_list[0][size - 1]:
        print('Diagonal 2 does not work! ')
        print('These are the values in diagonal 2: ', end = '')
        print(f'{init_list[i][(size - 1) - i]}')

if (init_list[j][i] == magic_number) and (init_list[j][i] == magic_number) and (init_list[i][i] == magic_number) and (init_list[i][(size - 1) - i] == magic_number):
    print('This is a magic square!')
else:
    print('This is not a magic square!')
