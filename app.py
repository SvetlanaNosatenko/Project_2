import json

from flask import Flask, render_template, request

app = Flask(__name__)


with open('data.json', encoding='utf-8') as f:
    posts = json.load(f)

with open('comments.json', encoding='utf-8') as f:
    comments = json.load(f)


@app.route('/')
def all_posts():
    return render_template("index.html", posts=posts)


@app.route('/posts/<int:postid>')
def one_post(postid: int):

        comments_id = []
        post_id = []

        for post in posts:
            if post["pk"] == postid:
                post_id.append(post)
        for comment in comments:
            if comment["post_id"] == postid:
                comments_id.append(comment)
        return render_template("post.html", comments=comments_id, count_comments=len(comments_id), posts=post_id)


@app.route('/search/')
def found_post():
    input_text = str(request.args.get('input_text'))
    response = []
    for post in posts:
        for i in post["content"].split(' '):
            if i.lower() == input_text.lower():
                response.append(post)
    return render_template("search.html", posts=response, сount_posts=len(response))


@app.route('/users/<username>')
def user_feed(username):
    name_post = []
    for post in posts:
        if post["poster_name"] == username:
            name_post.append(post)
    return render_template("user-feed.html", posts=name_post)



app.run()
