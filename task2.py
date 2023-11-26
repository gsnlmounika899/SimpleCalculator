class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        try:
            return self.a + self.b
        except TypeError as e:
            print(f"Error: {e}")
            return None

    def subtraction(self):
        try:
            return self.a - self.b
        except TypeError as e:
            print(f"Error: {e}")
            return None

    def multiplication(self):
        try:
            return self.a * self.b
        except TypeError as e:
            print(f"Error: {e}")
            return None

    def division(self):
        try:
            if self.b == 0:
                raise ZeroDivisionError("Division by 0 is not possible")
            return self.a / self.b
        except (TypeError, ZeroDivisionError) as e:
            print(f"Error: {e}")
            return None

def get_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

a = get_input("Enter the first number: ")
b = get_input("Enter the second number: ")
operator = input("Select your required operator (+, -, *, /): ")

c = Calculator(a, b)

if operator == '+':
    print(c.addition())
elif operator == '-':
    print(c.subtraction())
elif operator == '*':
    print(c.multiplication())
elif operator == '/':
    print(c.division())
else:
    print("Invalid operator selected.")
