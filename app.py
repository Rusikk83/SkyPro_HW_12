from flask import Flask, request, render_template, send_from_directory
from loader.loader import loader_blueprint
from main.main import list_blueprint


app = Flask(__name__)

app.register_blueprint(loader_blueprint)  #регистрируем блюпринт loader
app.register_blueprint(list_blueprint)  #регистрируем блюпринт main


"""Представление для страницы поиска"""
@app.route("/")
def page_index():
    return render_template("index.html")


"""Представление для доступа к файлам"""
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()


