import json


def load_posts(file_name="posts.json"):
    with open(file_name, encoding='utf-8') as file:
        data = file.read()
    posts = json.loads(data)
    return posts


def posts_find(posts, find_text):
    find_posts = []
    for el in posts:
        if find_text in el["content"]:
            find_posts.append(el)
    return find_posts


postss = load_posts()

print(postss)

with open(file='posts.json', mode="w", encoding='utf-8') as file:
    json.dump(postss, file, ensure_ascii=False)