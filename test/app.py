from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def index():
    with app.open_resource('mock/index.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        notice = json_dict['notice']
        movie = json_dict['movie']
        article = json_dict['article']
        photo = json_dict['photo']
        animes = json_dict['animes']
        courses = json_dict['courses']
    return render_template("index.html", notice=notice,movie=movie,article=article,photo=photo,animes=animes,courses=courses)

@app.route("/notices")
def notices():
    with app.open_resource('mock/notices.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        notices = json_dict['notices']
    return render_template("notices.html", notices=notices)

@app.route("/courses")
def courses():
    with app.open_resource('mock/courses.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        courses = json_dict['courses']
        name = json_dict['name']
    return render_template("courses.html", courses=courses,name=name)


@app.route("/movies/")
def movies():
    with app.open_resource('mock/movies.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        movies = json_dict['movies']
        name = json_dict['name']
    return render_template("movies.html", movies=movies, name=name)


@app.route("/animes/")
def animes():
    with app.open_resource('mock/animes.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        animes = json_dict['animes']
        name = json_dict['name']
    return render_template("animes.html", animes=animes,name=name)


@app.route("/photos/")
def photos():
    with app.open_resource('mock/photos.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        photos = json_dict['photos']
        name = json_dict['name']
    return render_template("photos.html", photos=photos,name=name)

@app.route("/articles")
def articles():
    with app.open_resource('mock/articles.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        articles = json_dict['articles']
    return render_template("articles.html", articles=articles)


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
