def fib_eo(n):
    """Функция для определения четности n-го числа Фибоначчи"""
    if n < 0:
        raise ValueError ( "n должно быть больше или равно 0" )

    # Последние цифры двух первых чисел Фибоначчи
    a , b = 0 , 1

    # Циклическое вычисление последней цифры
    for _ in range ( n ):  # итерация от 0 до n-1
        a , b = b , (a + b) % 10

    # Последняя цифра n-го числа
    last_digit = a

    # Определение четности
    return "even" if last_digit % 2 == 0 else "odd"


# Тестовая функция
def test_fib_eo():
    """Примеры для проверки"""
    test_cases = [1 , 2 , 10 , 841645 , 1000000]
    results = {n: fib_eo ( n ) for n in test_cases}
    return results


if __name__ == "__main__":
    print ( "Результаты проверки четности:" )
    results = test_fib_eo ()
    for n , parity in results.items ():
        print ( f"n={n}: {parity}" )
