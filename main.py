from pathlib import Path

# Создаем путь к папке files
files_dir = Path('files')
# если папка отсуттсвует, чтобы не выдавало ошибки, если присутствует то мы ее заново не пересоздаем и не перезаписываем ее содержимое
files_dir.mkdir(exist_ok=True)

# создаем пути для 2-х файлов
first_file = Path(files_dir / 'first.txt')
second_file = Path(files_dir / 'second.txt')

# Создаем файл first.txt и записываем в него данные, открываем в режиме записи и формируем две строки
with open(first_file, 'w') as f:
    f.write("First line\n")
    f.write("Second line\n")

# Создаем файл second.txt и записываем в него данные
with open(second_file, 'w') as f:
    lines = [
        "First line in second file",
        "Second line in second file",
        "Last line in second file"
    ]

    for line in lines:
        f.write(line + '\n')

# Читаем и выводим содержимое файла first.txt
with open(first_file) as f:
    print(f.read())

with open(second_file) as f:
    for line in f.readlines():
        print(line)

# удаляем оба файла
first_file.unlink()
second_file.unlink()

# удаление директории
files_dir.rmdir()
