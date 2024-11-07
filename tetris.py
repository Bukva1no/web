import re

def string_operations():
    # Основные операции со строками
    str1 = "Hello, World!"
    str2 = "Python is great."

    print("1. Основные операции со строками:")
    print("Строка 1:", str1)
    print("Строка 2:", str2)

    # Конкатенация
    concatenated = str1 + " " + str2
    print("Конкатенация:", concatenated)

    # Доступ к символам
    print("Первый символ строки 1:", str1[0])
    print("Последний символ строки 2:", str2[-1])

    # Срезы
    print("Срез строки 1 (1-5):", str1[1:5])
    print("Срез строки 2 (7-):", str2[7:])

def string_formatting():
    # Форматирование строк
    name = "Alice"
    age = 30
    formatted_string = f"My name is {name} and I am {age} years old."
    print("\n2. Форматирование строк:")
    print(formatted_string)

def multiline_strings():
    # Многострочные строки
    multiline_string = """Это многострочная строка.
    Она может занимать несколько строк.
    Удобно для длинных текстов."""
    print("\n3. Многострочные строки:")
    print(multiline_string)

def string_methods():
    # Методы строк
    text = "  python programming  "
    print("\n4. Методы строк:")
    print("Исходный текст:", text)
    print("Длина текста:", len(text))
    print("Приведение к верхнему регистру:", text.upper())
    print("Приведение к нижнему регистру:", text.lower())
    print("Удаление пробелов:", text.strip())
    print("Замена 'python' на 'Java':", text.replace("python", "Java"))

def regex_example():
    # Регулярные выражения
    text = "Email: example@example.com, Phone: 123-456-7890"
    print("\n5. Регулярные выражения:")
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'\d{3}-\d{3}-\d{4}'

    email_matches = re.findall(email_pattern, text)
    phone_matches = re.findall(phone_pattern, text)

    print("Найденные email адреса:", email_matches)
    print("Найденные номера телефонов:", phone_matches)

def file_operations():
    # Чтение и запись текстовых файлов
    print("\n6. Чтение и запись текстовых файлов:")
    with open("example.txt", "w") as f:
        f.write("Привет, мир!\nЭто пример записи в файл.")
    
    with open("example.txt", "r") as f:
        content = f.read()
        print("Содержимое файла example.txt:")
        print(content)

def encoding_decoding():
    # Кодирование и декодирование строк
    original_text = "Привет, мир!"
    encoded_text = original_text.encode('utf-8')
    decoded_text = encoded_text.decode('utf-8')

    print("\n7. Кодирование и декодирование строк:")
    print("Оригинальный текст:", original_text)
    print("Закодированный текст (bytes):", encoded_text)
    print("Декодированный текст:", decoded_text)

if __name__ == "__main__":
    string_operations()
    string_formatting()
    multiline_strings()
    string_methods()
    regex_example()
    file_operations()
    encoding_decoding()
