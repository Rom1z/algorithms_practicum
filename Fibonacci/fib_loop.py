import time


def fib(n):
    """Функция для вычисления n-го числа Фибоначчи с использованием цикла"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    prev , curr = 0 , 1
    for _ in range ( 2 , n + 1 ):
        prev , curr = curr , prev + curr
    return curr


def measure_execution_time():
    """Функция для замера времени выполнения алгоритма"""
    test_cases = [10 , 15 , 20 , 25 , 32]
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
    print ( "Замеры времени выполнения для разных n:" )
    results = measure_execution_time ()
    for n , data in results.items ():
        print ( f"n={n}: F(n)={data['result']}, время выполнения={data['time_ms']} ms" )
