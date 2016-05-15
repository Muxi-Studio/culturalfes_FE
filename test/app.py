#-*- coding: utf-8 -*-
from flask import Flask, render_template, request, session
import json, random
from geetest import GeetestLib

captcha_id = "b46d1900d0a894591916ea94ea91bd2c"
private_key = "36fc3fe98530eea08dfc6ce76e3d24c4"
user_id = random.randint(1,100) 

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a hard to guess string'

@app.route("/")
def index():
    with app.open_resource('mock/index.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        notices = json_dict['notices']
        movies = json_dict['movies']
        articles = json_dict['articles']
        photos = json_dict['photos']
        animes = json_dict['animes']
        courses = json_dict['courses']
    return render_template("index.html", notices=notices,movies=movies,articles=articles,photos=photos,animes=animes,courses=courses)

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
    return render_template("courses.html", courses=courses)


@app.route("/movies/")
def movies():
    with app.open_resource('mock/movies.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        movies = json_dict['movies']
    return render_template("movies.html", movies=movies)


@app.route("/animes/")
def animes():
    with app.open_resource('mock/animes.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        animes = json_dict['animes']
    return render_template("animes.html", animes=animes)


@app.route("/photos/")
def photos():
    with app.open_resource('mock/photos.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        photos = json_dict['photos']
    return render_template("photos.html", photos=photos)

@app.route("/articles")
def articles():
    with app.open_resource('mock/articles.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        articles = json_dict['articles']
    return render_template("articles.html", articles=articles)


@app.route("/photo/")
def photo():
    with app.open_resource('mock/photo.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        photo = json_dict['photo']
    return render_template("photo.html",photo=photo)


@app.route("/course/")
def course():
    with app.open_resource('mock/course.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        course = json_dict['course']
    return render_template("course.html", course=course)


@app.route("/movie/")
def movie():
    with app.open_resource('mock/movie.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        movie = json_dict['movie']
    return render_template("movie.html", movie=movie)


@app.route("/article/")
def article():
    with app.open_resource('mock/article.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        article = json_dict['article']
    return render_template("article.html", article=article)


@app.route("/anime/")
def anime():
    with app.open_resource('mock/anime.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        anime = json_dict['anime']
    return render_template("anime.html", anime=anime)

@app.route("/notice/")
def notice():
    with app.open_resource('mock/notice.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        notice = json_dict['notice']
    return render_template("notice.html", notice=notice)


@app.route("/rank")
def rank():
    with app.open_resource('mock/rank.json') as f:
        data = f.read()
        json_dict = json.loads(data)
        rank_movie = json_dict['rank_movie']
        rank_anime = json_dict['rank_anime']
        rank_photo = json_dict['rank_photo']
        rank_article = json_dict['rank_article']
        rank_course = json_dict['rank_course']
    return render_template("rank.html", rank_movie=rank_movie,rank_article=rank_article,rank_anime=rank_anime,rank_course=rank_course,rank_photo=rank_photo,)

@app.route("/upload/", methods=["POST", "GET"])
def upload():
    return render_template("upload.html")

@app.route('/getcaptcha/', methods=["GET"])
def get_captcha():
    user_id = random.randint(1,100)
    gt =  GeetestLib(captcha_id, private_key)
    status = gt.pre_process(user_id)
    session[gt.GT_STATUS_SESSION_KEY] = status
    session["user_id"] = user_id
    response_str = gt.get_response_str()
    return response_str


@app.route('/validate', methods=["POST"])
def validate_capthca():
    gt = GeetestLib(captcha_id, private_key)
    challenge = request.form[gt.FN_CHALLENGE]
    validate = request.form[gt.FN_VALIDATE]
    seccode = request.form[gt.FN_SECCODE]
    status = session[gt.GT_STATUS_SESSION_KEY]
    user_id = session["user_id"]
    if status:
        result = gt.success_validate(challenge, validate, seccode, user_id)
    else:
        result = gt.failback_validate(challenge, validate, seccode)
    result = "success" if result else "fail"
    if result == "success":
        return redirect(url_for("index"))
    else:
        flash("验证码错误!")
        return redirect(url_for("captcha"))



if __name__ == '__main__':
    app.run(debug=True)
