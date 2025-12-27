from flask import Flask, render_template, send_from_directory, jsonify
import os

BASE_DIR = "services/data/"
FILMS_DIR = os.path.join(BASE_DIR, "Films")
SERIES_DIR = os.path.join(BASE_DIR, "Series")

app = Flask(__name__)

# -------- HUB ----------

@app.route("/")
def index():
    return render_template("index.html")

# -------- FILMS --------

@app.route("/movies")
def movies():
    movies = []
    if os.path.exists(FILMS_DIR):
        for f in os.listdir(FILMS_DIR):
            if f.endswith(".mp4"):
                name = f[:-4]
                cover = f"{name}.jpg"
                movies.append({
                    "file": f,
                    "title": name,
                    "cover": cover if os.path.exists(os.path.join(FILMS_DIR, cover)) else None
                })
    return render_template("movies.html", movies=movies, active_page='movies')


@app.route("/play/movie/<name>")
def play_movie(name):
    return render_template("player.html", name=name, type="movie")

@app.route("/video/movie/<name>")
def movie_file(name):
    return send_from_directory(FILMS_DIR, name)

# -------- SERIES --------

@app.route("/series")
def series():
    shows = []
    if os.path.exists(SERIES_DIR):
        for show in os.listdir(SERIES_DIR):
            cover = os.path.join(SERIES_DIR, show, "cover.jpg")
            shows.append({
                "name": show,
                "cover": "/video/series-cover/" + show if os.path.exists(cover) else None
            })
    return render_template("series.html", shows=shows, active_page='series')

@app.route("/series/<show>")
def season_selector(show):
    show_path = os.path.join(SERIES_DIR, show)

    if not os.path.exists(show_path):
        return "Series not available", 404

    seasons = sorted([
        d for d in os.listdir(show_path)
        if os.path.isdir(os.path.join(show_path, d))
    ])

    first_season = seasons[0] if seasons else None
    episodes = []

    if first_season:
        season_path = os.path.join(show_path, first_season)
        episodes = sorted([
            f for f in os.listdir(season_path)
            if f.endswith(".mp4")
        ])

    return render_template(
        "season_selector.html",
        series_name=show,
        seasons=seasons,
        first_season=first_season,
        episodes=episodes,
        active_page="season_selection"
    )


@app.route("/series/<show>/episodes/<season>")
def get_episodes(show, season):
    season_path = os.path.join(SERIES_DIR, show, season)

    if not os.path.exists(season_path):
        return jsonify({"episodes": []})

    episodes = sorted([
        f for f in os.listdir(season_path)
        if f.endswith(".mp4")
    ])

    return jsonify({"episodes": episodes})

@app.route("/video/series-cover/<show>")
def series_cover(show):
    return send_from_directory(
        os.path.join(SERIES_DIR, show),
        "cover.jpg"
    )


@app.route("/play/episode/<show>/<season>/<episode>")
def play_episode(show, season, episode):
    return render_template(
        "player.html",
        name=episode,
        type="episode",
        show=show,
        season=season
    )

@app.route("/video/episode/<show>/<season>/<episode>")
def episode_file(show, season, episode):
    return send_from_directory(
        os.path.join(SERIES_DIR, show, season),
        episode
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


