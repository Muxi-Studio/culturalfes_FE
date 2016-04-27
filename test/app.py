from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def index():
    with app.open_resource('mock/courses.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        info = json_dict['info']
        hot_comments = json_dict['hot_comments']
    return render_template("index.html", info=info, hot_comments=hot_comments)
# something wrong!
@app.route("/courses")
def courses():
    with app.open_resource('mock/courses.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        info = json_dict['info']
        hot_comments = json_dict['hot_comments']
    return render_template("upload.html", info=info, hot_comments=hot_comments)


@app.route("/movies/")
def movies():
    with app.open_resource('mock/movies.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        info = json_dict['info']

    return render_template("movies.html", info=info, hot_comments=hot_comments)


@app.route("/animes/")
def animes():
    with app.open_resource('mock/animes.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        info = json_dict['info']
    return render_template("animes.html", info=info)


@app.route("/photos/")
def photos():
    with app.open_resource('mock/photos.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        info = json_dict['info']
    return render_template("photos.html", info=info)


@app.route("/articles")
def articles():
    with app.open_resource('mock/articles.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        info = json_dict['info']
    return render_template("articles.html", info=info)


@app.route("/photo/<int:id>/")
def photo():
    with app.open_resource('mock/photo.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        info = json_dict['info']
    return render_template("photo.html", info=info)


@app.route("/course/<int:id>/")
def course():
    with app.open_resource('mock/course.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        info = json_dict['info']
    return render_template("course.html", info=info)


@app.route("/movie/<int:id>/")
def movie():
    with app.open_resource('mock/movie.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        info = json_dict['info']
    return render_template("movie.html", info=info)


@app.route("/article/<int:id>/")
def article():
    with app.open_resource('mock/article.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        info = json_dict['info']
    return render_template("article.html", info=info)


@app.route("/anime/<int:id>/")
def anime():
    with app.open_resource('mock/anime.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        info = json_dict['info']
    return render_template("anime.html", info=info)


if __name__ == '__main__':
    app.run(debug=True)
