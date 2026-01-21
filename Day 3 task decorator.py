import time

# Decorator to measure execution time
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"Function Name: {func.__name__}")
        print(f"Execution Time: {end_time - start_time:.6f} seconds")

        return result
    return wrapper


# Function to write numbers 1–100 into a file
def write_numbers_to_file(filename):
    with open(filename, "w") as file:
        for i in range(1, 101):
            file.write(str(i) + "\n")


# Apply decorator to recursive factorial function
@execution_time
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Testing
print("Factorial Result:", factorial(5))
