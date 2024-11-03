import os

directory = "."
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(directory, file)
        import time
        if os.path.exists(filepath):
            filetime = os.path.getmtime(file)
            formatted_time = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(filetime))
            file_size = os.path.getsize(file)
            parent_dir = os.path.dirname(filepath)
            print(
                f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: {formatted_time}, '
                f'Родительская директория: {parent_dir}')

