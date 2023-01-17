from flask import Blueprint, request, render_template
from functions import *
import logging


loader_blueprint = Blueprint('loader_blueprint', __name__)
logging.basicConfig(level=logging.INFO)


"""Представление для страницы загрузки нового поста и страницы подтверждения загрузки поста"""
@loader_blueprint.route("/post", methods=["GET", "POST"])
def page_post_form():
    if request.method == "GET":
        return render_template("post_form.html")
    else:
        picture = request.files.get("picture")
        if picture.filename.split(".")[-1] not in {'png', 'jpg', 'jpeg', 'gif'}:
            logging.info(f"Файл {picture.filename}не является картинкой")
            return f"Файл {picture.filename} не является картинкой"
        path = f"uploads/images/{picture.filename}"
        picture.save(path)
        content = request.values.get('content')
        posts = load_posts()
        posts.append({
                       "pic": path,
                       "content": content
                     })
        with open(file='posts.json', mode="w", encoding='utf-8') as file:
            json.dump(posts, file, ensure_ascii=False)
        return render_template("post_uploaded.html", img_path=path, content=content)


