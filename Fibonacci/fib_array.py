def fib(n):
    """Функция для вычисления чисел Фибоначчи с записью в массив"""
    if n < 0:
        return []

    # Инициализация массива
    fib_sequence = [0] * (n + 1)

    # Задание начальных условий
    if n >= 1:
        fib_sequence[1] = 1

    # Вычисление чисел Фибоначчи
    for i in range(2, n + 1):
        fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2]

    return fib_sequence

def measure_execution_time():
    """Замер времени выполнения"""
    import time
    test_cases = [10, 15, 20, 30, 40]
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
    print("Числовые ряды Фибоначчи для заданных n:")
    test_cases = [8, 10, 15]
    for n in test_cases:
        print(f"n={n}: {fib(n)}")

    print("\nЗамеры времени выполнения:")
    results = measure_execution_time()
    for n, data in results.items():
        print(f"n={n}: Последнее число F(n)={data['result'][-1]}, время выполнения={data['time_ms']} ms")
