import math


def fib(n):
    """Функция для вычисления n-го числа Фибоначчи с использованием формулы Бине"""
    if n < 0:
        raise ValueError ( "n должно быть больше или равно 0" )

    # Формула Бине
    sqrt_5 = math.sqrt ( 5 )
    phi = (1 + sqrt_5) / 2  # Золотое сечение
    psi = (1 - sqrt_5) / 2

    # Вычисление числа Фибоначчи с округлением
    fib_n = (phi ** n - psi ** n) / sqrt_5
    return round ( fib_n )


def measure_execution_time():
    """Замер времени выполнения"""
    import time
    test_cases = [10 , 20 , 32 , 50 , 64]
    results = {}

    for n in test_cases:
        start_time = time.time ()
        result = fib ( n )
        end_time = time.time ()
        execution_time = (end_time - start_time) * 1000  # перевод в миллисекунды
        results[n] = {
            "result": result ,
            "time_ms": round ( execution_time , 3 )
        }

    return results


if __name__ == "__main__":
    print ( "Результаты вычисления чисел Фибоначчи с использованием формулы Бине:" )
    test_cases = [10 , 32 , 50]
    for n in test_cases:
        print ( f"n={n}: F(n)={fib ( n )}" )

    print ( "\nЗамеры времени выполнения:" )
    results = measure_execution_time ()
    for n , data in results.items ():
        print ( f"n={n}: F(n)={data['result']}, время выполнения={data['time_ms']} ms" )
