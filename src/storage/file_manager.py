# src/storage/file_manager.py
import os

def save_config(user_id, username, game, file_content):
    # Директория для хранения файлов
    user_dir = f'src/storage/configs/{username}'
    os.makedirs(user_dir, exist_ok=True)

    # Путь к файлу конфига
    config_path = os.path.join(user_dir, f'{game}.cfg')

    # Сохраняем конфиг на сервере
    with open(config_path, 'wb') as config_file:
        config_file.write(file_content)

    # TODO: Добавить логику для обновления записи в базе данных
