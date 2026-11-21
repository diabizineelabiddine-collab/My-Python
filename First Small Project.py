# First Project: A Simple Calculator
import Operations

# تنظيم الرموز على شك لقائمة
Operation_odd = ['%','π','^2','^3','²√','³√']
Operation_even = ['+','-','*','/']
Operation = Operation_odd + Operation_even

while True:
 # إظهار رسالة ترحيب
 print('\nWelcome to the Simple Calculator Program!\n')
 print('What would you like to calculate today?\nWe have many options available!\n')
 #
 choise = input(f'Please choose one of the following options: {Operations.list_to_string(Operation)}\n').strip()

 # التحقق من إدخال المستخدم للإختيارات المتاحة
 while choise not in Operation:
    print(f'\nInvalid option!\n')
    choise = input(f'Please choose one of the following options: {Operations.list_to_string(Operation)}\n').strip()

 # إدخال الأعداد
 else:
    b = None

    if choise in Operation_even:
      a = Operations.get_number('Please enter the first number: ')
      b = Operations.get_number('Please enter the second number: ')

    else:
        a = Operations.get_number('Please enter a number: ')

 # تنفيذ و عرض النتيجة
 Operations.show_result_message()

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

 # عرض رسالة شكر
 Operations.show_goodbye_message()

 choice = input(f'\nWould you like to continue? (Yes/No): ').strip().lower()

 if choice  != 'yes':
     print('\nAlright, as you wish, and thank you once again for using my program!')
     break


