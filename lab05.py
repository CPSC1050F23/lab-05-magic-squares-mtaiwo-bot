"""
Author:         Folu Taiwo
Date:           9/26/23
Assignment:     Lab 05
Course:         CPSC1051
Lab Section:    003

CODE DESCRIPTION: Asks user for size of a magic square and creates the 
square with all rows, columns, and diagonals adding up to the magic number.

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
print(f'The magic number for size {size} is {magic_number:.0f}.')

#Enter the magic square as a list of numbers
print('Enter in the values separated by spaces: ')
values = input().split()
value_list = [] 
input_square = []

for i in range(len(values)):
    value_list.append(int(values[i]))
    if i % size == size - 1:
        input_square.append(value_list)
        value_list = []

#printing a 2d array (list)
print('Your square:')
for i in range(size):
    for j in range(size):
        print(f'{input_square[i][j]}',end=" ") 
    print('\n')

    
# Generate the expected list with numbers 1 to n^2
expected_list = []
for i in range (1,size**2+1):
    expected_list.append(i)

input_list=[]
for i in range (len(input_square)):
    for j in range (len(input_square)):
        input_list.append(input_square[i][j])
    
# Check if the sorted lists are equal
input_list.sort()
if input_list != expected_list:
    print(f'The input cannot be a magic square! There must be one of each value from 1 to {size**2}.')
    

#Check rows
for i in range(len(input_square)):
    row_string=""
    total_row=0
    for num in input_square[i]:
        total_row += num
        row_string += str(num) + " "
    if total_row != magic_number:
        print(f'Row {i} does not work! These are the values in row {i}: {row_string}')   

    
# Check columns
for j in range(len(input_square)):
    column_string=""
    total_column=0
    for j in range (len(input_square)):
        total_column += input_square[j][i]
        column_string += str(input_square[j][i]) + " "
    if total_column != magic_number:
        print(f'Column {i} does not work! These are the values in column {i}: {column_string}')


#Check upper to lower diagonal
diagonal_string=""
total_diagonal=0
for i in range(len(input_square)):
    total_diagonal += input_square[i][i]
    diagonal_string += str(input_square[i][i]) + " "
if total_diagonal != magic_number:
    print('Diagonal 1 does not work! ')
    print(f'These are the values in diagonal 1: {diagonal_string}')

#Check lower to upper diagonal
diagonal_string=""
total_diagonal=0
for i in range(len(input_square)):
    total_diagonal += input_square[i][size - 1 - i]
    diagonal_string += str(input_square[i][size - 1 - i]) + " "
if total_diagonal != magic_number:
    print('Diagonal 2 does not work! ')
    print(f'These are the values in diagonal 2: {diagonal_string}')


if total_diagonal == total_column:
    print('This is a magic square!')
else:
    print('This is not a magic square!')
