def huffman_decode():
    """Функция для декодирования строки по алгоритму Хаффмана"""
    # Входные данные
    data = """12 60
' ': 1011
'.': 1110
'D': 1000
'c': 000
'd': 001
'e': 1001
'i': 010
'm': 1100
'n': 1010
'o': 1111
's': 011
'u': 1101
100011110001001101000111111011001010011000010110011010111110"""
    lines = data.splitlines ()

    # Разбор входных данных
    header = lines[0]
    encoded_string = lines[-1]
    code_map = {}

    for line in lines[1:-1]:
        symbol , code = line.split ( ": " )
        symbol = symbol.strip ( "'" )
        code_map[code] = symbol

    # Декодирование строки
    decoded_string = []
    temp_code = ""

    for bit in encoded_string:
        temp_code += bit
        if temp_code in code_map:
            decoded_string.append ( code_map[temp_code] )
            temp_code = ""

    # Вывод результата
    decoded_result = "".join ( decoded_string )
    print ( decoded_result )
    return decoded_result


if __name__ == "__main__":
    huffman_decode ()
