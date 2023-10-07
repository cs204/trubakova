def main():
    file_name = input("File name: ")

    # Используем словарь для соответствия расширений и медиа типов
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    # Ищем расширение в имени файла
    file_extension = file_name[file_name.rfind("."):]

    # Проверяем, есть ли соответствие в словаре
    media_type = media_types.get(file_extension, "application/octet-stream")

    print(media_type)

if __name__ == "__main__":
    main()