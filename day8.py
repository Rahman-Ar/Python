#Error handling
def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        result = None
    except ValueError:
        print("Error: Invalid value.")
        result = None
    else:
        print(f"Result: {result}")
    finally:
        print("Execution completed.")
    return result

# Test cases
divide_numbers(10, 2)  
divide_numbers(10, 0)  