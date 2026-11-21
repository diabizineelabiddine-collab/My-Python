import math

# التحقق من إدخال عدد عشري
def get_integer(message):
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
    while True:
        try:
            return a/b
        except ZeroDivisionError:
            show_zero_division_error()
            return None

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
    return a**(1/2)

# حساب الجذر التكعيبي
def cube_root(a):
    return a**(1/3)

# حساب ضرب π
def pi(a):
    return a*math.pi











