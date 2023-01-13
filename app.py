import json

from flask import Flask, request, render_template, send_from_directory
from functions import *

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template("index.html")


@app.route("/list")
def page_tag():
    find_text = request.args.get("s")
    posts = posts_find(load_posts(), find_text)
    return render_template("post_list.html", items=posts, find_text=find_text)


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    if request.method == "GET":
        return render_template("post_form.html")
    else:
        picture = request.files.get("picture")
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





@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()


