from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def index():
    with app.open_resource('mock/courses.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        notice = json_dict['notice']
        movie = json_dict['movie']
        article = json_dict['article']
        photo = json_dict['photo']
        comic = json_dict['comic']
        micromovie = json_dict['micromovie']
    return render_template("index.html", notice=notice,movie=movie,article=article,photo=photo,comic=comic,micromovie=micromovie,)

@app.route("/courses")
def courses():
    with app.open_resource('mock/courses.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        info = json_dict['info']
        hot_comments = json_dict['hot_comments']
    return render_template("courses.html", info=info, hot_comments=hot_comments)


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

@app.route("/second")
def second():
     with app.open_resource('mock/article.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        article = json_dict['article']
    return render_template("second.html",article=article)

@app.route("/rank")
def rank():
    with app.open_resource('mock/rank.json') as f:
        date = f.read()
        json_dict = json.loads(data)
        rank_movie = json_dict['rank_movie']
        rank_comic = json_dict['rank_comic']
        rank_photo = json_dict['rank_photo']
        rank_article = json_dict['rank_article']
        rank_miniclass = json_dict['rank_miniclass']
    return render_template("rank.html", rank_movie=rank_movie,rank_article=rank_article,rank_comic=rank_comic,rank_miniclass=rank_miniclass,rank_photo=rank_photo,)
@app.route("/upload")

def upload():
    return render_template("upload.html")


if __name__ == '__main__':
    app.run(debug=True)
