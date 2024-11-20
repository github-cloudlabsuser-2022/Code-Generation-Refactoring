# Create a basic calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def solve_linear_equation(a, b):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero")
    return -b / a

# Example usage:
if __name__ == "__main__":
    print("Addition: ", add(5, 3))
    print("Subtraction: ", subtract(5, 3))
    print("Multiplication: ", multiply(5, 3))
    print("Division: ", divide(5, 3))
    print("Solving equation 2x + 3 = 0: x =", solve_linear_equation(2, 3))




