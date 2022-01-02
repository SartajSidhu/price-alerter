from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sartaj is best'
    app.config['SERVER_NAME'] = 'localhost:5000'

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app
