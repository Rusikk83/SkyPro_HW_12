import json
import logging
from json import JSONDecodeError


logging.basicConfig(level=logging.ERROR)


def load_posts(file_name="posts.json"):
    """Загружает список постов из файла. Возвращает список всех постов из файла"""
    try:
        with open(file_name, encoding='utf-8') as file:
            data = file.read()

    except FileNotFoundError:
        logging.error("Ошибка доступа к файлу")
        return []

    try:
        posts = json.loads(data)
        return posts

    except JSONDecodeError:
        # Будет выполнено если файл найден, но не превращается из JSON
        logging.error("Файл не удается преобразовать")
        return []


def posts_find(posts, find_text):
    """Производит поиск постов по вхождению строки. Возвращает список постов"""
    find_posts = []
    for el in posts:
        if find_text in el["content"]:
            find_posts.append(el)
    return find_posts
