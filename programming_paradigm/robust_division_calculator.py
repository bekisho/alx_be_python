# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")

if __name__ == "__main__":
    num_input = input("Enter numerator: ")
    denom_input = input("Enter denominator: ")
    safe_divide(num_input, denom_input)
