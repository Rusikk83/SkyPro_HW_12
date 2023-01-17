from flask import Blueprint, render_template, request
from functions import *
import logging

list_blueprint = Blueprint("list_blueprint", __name__)

logging.basicConfig(level=logging.INFO)


"""Представление для страницы с результатом поиска постов"""
@list_blueprint.route("/list")
def page_tag():
    find_text = request.args.get("s")
    logging.info(f"Выполнен поиск по строке: {find_text}")
    posts = posts_find(load_posts(), find_text)
    return render_template("post_list.html", items=posts, find_text=find_text)
