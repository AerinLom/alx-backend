#!/usr/bin/env python3
"""
Flask app with parametrized templates using gettext and mock login
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _
from typing import Union
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    return render_template('5-index.html')


def get_user() -> Union[dict, None]:
    """
    Returns user dict if ID can be found
    """
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)
    else:
        return None


@app.before_request
def before_request():
    """
    Finds user and sets as global on flask.g.user
    """
    g.user = get_user()


if __name__ == '__main__':
    app.run(debug=True)
