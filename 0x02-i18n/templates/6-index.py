<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,
    initial-scale=1.0, viewport-fit=cover">
    <title>{{ _('home_title') }}</title>
  </head>
  <body>
    <h1>{{ _('home_header') }}</h1>
    {% if g.user %}
    <p>{{ _('logged_in_as', username=g.user.get['name']) }}</p>
    {% else %}
    <p>{{ _('not_logged_in') }}</p>
    {% endif %}
  </body>
</html>
