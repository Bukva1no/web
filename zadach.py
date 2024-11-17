def add_numbers(a: int, b: int) -> int:
    return a + b

def sum_of_list(numbers: list) -> int:
    return sum(numbers)

def join_strings(separator: str, *args: str) -> str:
    return separator.join(args)

def split_string(input_string: str, delimiter: str) -> list:
    return input_string.split(delimiter)

# Примеры использования
# Пример использования add_numbers
result_add = add_numbers(5, 10)
print(f"Сумма чисел: {result_add}")

# Пример использования sum_of_list
result_sum = sum_of_list([1, 2, 3, 4, 5])
print(f"Сумма списка: {result_sum}")

# Пример использования join_strings
result_join = join_strings(", ", "apple", "banana", "cherry")
print(f"Объединенная строка: {result_join}")

# Пример использования split_string
result_split = split_string("apple,banana,cherry", ",")
print(f"Разделенный список: {result_split}")
