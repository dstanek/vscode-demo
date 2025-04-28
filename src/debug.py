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

def main():
    x = 10
    y = 5

    result_add = add(x, y)
    print(f"Addition: {x} + {y} = {result_add}")

    result_subtract = subtract(x, y)
    print(f"Subtraction: {x} - {y} = {result_subtract}")

    result_multiply = multiply(x, y)
    print(f"Multiplication: {x} * {y} = {result_multiply}")

    result_divide = divide(x, y)
    print(f"Division: {x} / {y} = {result_divide}")

if __name__ == "__main__":
    main()
