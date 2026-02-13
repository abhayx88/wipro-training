import time
import math
import sys
from multiprocessing import Pool, cpu_count

sys.set_int_max_str_digits(1000000)

numbers = [50000, 60000, 55000, 45000, 70000]

def calculate_factorial(n):
    return math.factorial(n)

if __name__ == "__main__":

    start_seq = time.perf_counter()

    seq_results = []
    for num in numbers:
        result = calculate_factorial(num)
        seq_results.append(result)
        print(f"Sequential -> Digits in factorial of {num}: {len(str(result))}")

    end_seq = time.perf_counter()
    print("\nSequential Time:", end_seq - start_seq)


    start_mp = time.perf_counter()

    with Pool(cpu_count()) as pool:
        mp_results = pool.map(calculate_factorial, numbers)

    for num, result in zip(numbers, mp_results):
        print(f"Multiprocessing -> Digits in factorial of {num}: {len(str(result))}")

    end_mp = time.perf_counter()
    print("\nMultiprocessing Time:", end_mp - start_mp)
