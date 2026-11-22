import math

def get_number(message):
    while True:
     try:
        return float(input(message))
     except ValueError:
                show_invalid_input_error()

# عرض رسالة خطأ عندما يُدخل المستخدم قيمة غير صالحة
def show_invalid_input_error():
    print("Invalid input! Please enter a valid value.")

# حساب الجمع
def add(a,b):
    return a+b

# حساب الطرح
def subtract(a,b):
    return a-b

# حساب الضرب
def multiply(a,b):
    return a*b

# حساب القسمة
def divide(a,b):
    while b == 0:
        show_zero_division_error()
        b = get_number('Please enter the divisor again:')

    return a/b

# عرض رسالة خطأ عند محاولة المستخدم القسمة على الصفر
def show_zero_division_error():
    print("Error: Division by zero is not allowed.")

# حساب النسبة المئوية
def percentage(a):
    return a/100

# حساب أس مربع
def square(a):
    return a**2

# حساب أس مكعب
def cube(a):
    return a**3

# حساب الجذر التربيعي
def square_root(a):
    while a < 0:
       show_square_root_error()
       a = get_number('\nPlease enter the square root again:')

    return a**(1/2)

# عرض رسالة خطأ عند محاولة حساب الجذر التربيعي لعدد سالب
def show_square_root_error():
    print('Error: Cannot calculate the square root of a negative number.')

# حساب الجذر التكعيبي
def cube_root(a):
    if a >= 0:
        return a**(1/3)
    else:
        return -(abs(a)**(1/3))

# حساب ضرب π
def pi(a):
    return a*math.pi

# عرض رسالة النتيجة
def show_result_message():
    print('\nThe result of the calculation is: ')

# عرض رسالة شكر للمستخدم عند الانتهاء من استخدام البرنامج
def show_goodbye_message():
    print('\nThank you for using my programme!')

# تحويل القائمة إلى سلسلة نصية
def list_to_string(variable):
    return ', '.join(variable)

# التحقق من إدخال المستخدم لعدد صحيح موجب
def get_positive_number(message):
    while True:
        try:
            number = int(input(message))

            if number < 0:
               raise ValueError('Please enter a positive number.')

            return number

        except ValueError:
            show_invalid_input_error()

# التحقق مما إذا كان المستخدم يرغب في مواصلة العملية أو لا وإرجاع قيمة منطقية (True أو False)
def continue_operation():
 while True:
    choice = input(f'\nWould you like to continue? (Yes/No): ').strip().lower()
    if choice in ['yes', 'no']:
        return choice == 'yes'
    print('Please enter yes or no.')

