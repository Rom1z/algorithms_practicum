import time

def fib(n):
    """Рекурсивная функция для вычисления n-го числа Фибоначчи"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def measure_execution_time():
    """Функция для замера времени выполнения алгоритма"""
    test_cases = [5, 10, 15, 20, 24]
    results = {}

    for n in test_cases:
        start_time = time.time()
        result = fib(n)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # перевод в миллисекунды
        results[n] = {
            "result": result,
            "time_ms": round(execution_time, 3)
        }

    return results

if __name__ == "__main__":
    print("Замеры времени выполнения для разных n:")
    results = measure_execution_time()
    for n, data in results.items():
        print(f"n={n}: F(n)={data['result']}, время выполнения={data['time_ms']} ms")
