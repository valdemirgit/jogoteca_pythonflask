from app.auth import auth as auth_blueprint
from .games import games as games_blueprint
from app.user import user as user_blueprint


def init_app(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(games_blueprint)
    app.register_blueprint(user_blueprint)
