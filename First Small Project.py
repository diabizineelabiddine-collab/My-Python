# First Project: A Simple Calculator

import Operations

Operation_odd = ['%','π','^2','^3','²√','³√']
Operation_even = ['+','-','*','/']
Operation = Operation_odd + Operation_even

print('Welcome to the Simple Calculator Program!\n')
print('What would you like to calculate today?\nWe have many options available!\n')

choise = input(f'Please choose one of the following options: {Operation}\n')

while choise not in Operation:
    print(f'\nInvalid option!\n')
    choise = input(f'Please choose one of the following options: {Operation}\n')

else:
    b = None

    if choise in Operation_even:
      a = Operations.get_integer('Please enter the first number: ')
      b = Operations.get_integer('Please enter the second number: ')

    else:
        a = Operations.get_integer('Please enter a number: ')

print('\nThe result of the calculation is:')

if choise == '+':
    print(Operations.add(a,b))
elif choise == '-':
    print(Operations.subtract(a,b))
elif choise == '*':
    print(Operations.multiply(a,b))
elif choise == '/':
    print(Operations.divide(a,b))
elif choise == '%':
    print(Operations.percentage(a))
elif choise == '^2':
    print(Operations.square(a))
elif choise == '^3':
    print(Operations.cube(a))
elif choise == '²√':
     print(Operations.square_root(a))
elif choise == 'π':
     print(Operations.pi(a))
else:
     print(Operations.cube_root(a))

print('\nThank you for using my programme!')