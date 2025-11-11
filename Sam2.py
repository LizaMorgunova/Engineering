class EmptyFileError(Exception):
    """Исключение, вызываемое при попытке прочитать пустой файл."""
    pass
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if not content:
                raise EmptyFileError("Файл пустой")
            print("Содержимое файла:")
            print(content)
    except EmptyFileError as e:
        print(e)
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    empty_file_path = 'empty_file.txt'
    non_empty_file_path = 'non_empty_file.txt'
    open(empty_file_path, 'w').close()
    with open(non_empty_file_path, 'w') as file:
        file.write("Это тестовое содержимое файла.")

    print("Чтение пустого файла:")
    read_file(empty_file_path)

    print("\nЧтение непустого файла:")
    read_file(non_empty_file_path)
