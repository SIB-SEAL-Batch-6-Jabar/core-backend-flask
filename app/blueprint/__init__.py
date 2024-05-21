from .user import UserBlueprint


class Blueprint:
    @staticmethod
    def register(app):
        # UserBlueprint.get("calculate").register(app, options={"url_prefix": "/"})
        app.register_blueprint(UserBlueprint)
