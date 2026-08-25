import time


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    num = 10
    start = time.perf_counter()
    result_rec = factorial_recursive(num)
    end = time.perf_counter()
    print(f"Recursive Factorial of {num} = {result_rec}  (Time: {end - start:.8f}s)")

    start = time.perf_counter()
    result_iter = factorial_iterative(num)
    end = time.perf_counter()
    print(f"Iterative Factorial of {num} = {result_iter}  (Time: {end - start:.8f}s)")
