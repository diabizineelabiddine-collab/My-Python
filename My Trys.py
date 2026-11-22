import Operations

def total_n1_df():

 while True:

  a = Operations.get_positive_number('\nEnter the number you want to start counting from: ')
  b = Operations.get_positive_number('Enter the number you want to stop counting from: ')

  while a > b:
    print("\nThe starting number must be less than or equal to the ending number.")
    a = Operations.get_positive_number('\nEnter the number you want to start counting from: ')
    b = Operations.get_positive_number('Enter the number you want to stop counting from: ')

  else:
   s = 0
   for i in range(a,b+1):
    s += i
   print(f'\nThe sum is: {s}')

   if not Operations.continue_operation():
       break


def total_n2_df():
  while True:
    a = Operations.get_positive_number('\nEnter the number you want to start counting from: ')
    b = Operations.get_positive_number('Enter the number you want to stop counting from: ')

    while a > b:
        print("\nThe starting number must be less than or equal to the ending number.")
        a = Operations.get_positive_number('\nEnter the number you want to start counting from: ')
        b = Operations.get_positive_number('Enter the number you want to stop counting from: ')


    else:
        s = ((b-a+1)*(a+b)/2)
        print(f'\nThe sum is: {s}')

    if not Operations.continue_operation():
        break


def total_n1():
  while True:
     a = Operations.get_positive_number('\nEnter the number you want to sum up to, starting from zero: ')
     s = 0
     for i in range(a+1):
        s += i
     print(f'\nThe sum is: {s}')

     if not Operations.continue_operation():
         break


def total_n2():
  while True:
      a = Operations.get_positive_number('\nEnter the number you want to sum up to, starting from zero: ')
      s = (a*(a+1)/2)
      print(f'\nThe sum is: {s}')

      if not Operations.continue_operation():
          break