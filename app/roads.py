import os

from flask import (
    Blueprint,
    render_template,
    send_from_directory,
    jsonify,
    request,
    redirect,
    url_for,
    current_app
)

from app.config_loader import load_config, save_config

roads = Blueprint("roads", __name__)


# ----------------
#      HUB
# ----------------

@roads.route("/")
def index():
    return render_template("index.html", active_page="home")


# ----------------
#      MOVIES
# ----------------

@roads.route("/movies")
def movies():
    movies = []

    media_root = current_app.config["MEDIA_PATH"]
    movies_dir = os.path.join(media_root, "Movies")

    if os.path.exists(movies_dir):
        for f in os.listdir(movies_dir):
            if f.endswith(".mp4"):
                name = f[:-4]
                cover = f"{name}.jpg"
                cover_path = os.path.join(movies_dir, cover)

                movies.append({
                    "file": f,
                    "title": name,
                    "cover": cover if os.path.exists(cover_path) else None
                })

    return render_template(
        "movies.html",
        movies=movies,
        active_page="movies"
    )


@roads.route("/play/movie/<name>")
def play_movie(name):
    return render_template(
        "player.html",
        name=name,
        type="movie"
    )


@roads.route("/video/movie/<name>")
def movie_file(name):
    movies_dir = os.path.join(current_app.config["MEDIA_PATH"], "Movies")
    return send_from_directory(movies_dir, name)


# ----------------
#      SERIES
# ----------------

@roads.route("/series")
def series():
    shows = []

    media_root = current_app.config["MEDIA_PATH"]
    series_dir = os.path.join(media_root, "Series")

    if os.path.exists(series_dir):
        for show in os.listdir(series_dir):
            show_path = os.path.join(series_dir, show)
            cover_path = os.path.join(show_path, "cover.jpg")

            if os.path.isdir(show_path):
                shows.append({
                    "name": show,
                    "cover": f"/video/series-cover/{show}"
                    if os.path.exists(cover_path) else None
                })

    return render_template(
        "series.html",
        shows=shows,
        active_page="series"
    )


@roads.route("/series/<show>")
def season_selector(show):
    series_dir = os.path.join(current_app.config["MEDIA_PATH"], "Series")
    show_path = os.path.join(series_dir, show)

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


@roads.route("/series/<show>/episodes/<season>")
def get_episodes(show, season):
    season_path = os.path.join(
        current_app.config["MEDIA_PATH"],
        "Series",
        show,
        season
    )

    if not os.path.exists(season_path):
        return jsonify({"episodes": []})

    episodes = sorted([
        f for f in os.listdir(season_path)
        if f.endswith(".mp4")
    ])

    return jsonify({"episodes": episodes})


@roads.route("/video/series-cover/<show>")
def series_cover(show):
    series_dir = os.path.join(current_app.config["MEDIA_PATH"], "Series")
    return send_from_directory(
        os.path.join(series_dir, show),
        "cover.jpg"
    )


@roads.route("/play/episode/<show>/<season>/<episode>")
def play_episode(show, season, episode):
    return render_template(
        "player.html",
        name=episode,
        type="episode",
        show=show,
        season=season
    )


@roads.route("/video/episode/<show>/<season>/<episode>")
def episode_file(show, season, episode):
    episode_dir = os.path.join(
        current_app.config["MEDIA_PATH"],
        "Series",
        show,
        season
    )
    return send_from_directory(episode_dir, episode)


# --------------------
#      SETTINGS
# --------------------

@roads.route("/settings")
def settings():
    config = load_config()
    return render_template(
        "settings.html",
        media_path=config["media_path"],
        active_page="settings"
    )


@roads.route("/settings/save", methods=["POST"])
def save_settings():
    config = load_config()
    new_path = request.form.get("media_path", "").strip()

    config["media_path"] = new_path
    save_config(config)

    return redirect(url_for("roads.settings"))


@roads.route("/settings/restart", methods=["POST"])
def restart_server():
    #print("[INFO] Restart requested")
    os._exit(42)


@roads.route("/settings/stop", methods=["POST"])
def stop_server():
    #print("[INFO] Server stopped")
    os._exit(0)
