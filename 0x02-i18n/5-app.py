#!/usr/bin/env python3
"""
Flask app with parametrized templates using gettext and mock login
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _


class Config:
    """
    Babel config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Mock login by user ID from URL parameter
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """
    Set user globally if logged in
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for supported languages.
    """
    if g.user and g.user['locale']:
        return g.user['locale']
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Index page with translated text and user info
    """
    if g.user:
        message = _(
            "You are logged in as {username}.".format(username=g.user['name'])
        )

    else:
        message = _("You are not logged in.")
    return render_template('5-index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
