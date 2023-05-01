import pytest
from flask import template_rendered
from contextlib import contextmanager
from webapp.thirdparties.flask import create_app
from webapp.thirdparties.flask.config import Config


class ConfigTest(Config):
    TESTING = True
    DB_URL = 'postgresql://postgres:postgres@localhost:5432/flasktestdb'


@pytest.fixture
def app():
    app = create_app(ConfigTest)
    return app

# https://stackoverflow.com/questions/39822265/flask-testing-how-to-retrieve-variables-that-were-passed-to-jinja
@contextmanager
def get_context_variables(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append(context)
    template_rendered.connect(record, app)
    try:
        yield iter(recorded)
    finally:
        template_rendered.disconnect(record, app)
