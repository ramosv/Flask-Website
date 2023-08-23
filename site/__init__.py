from flask import Flask


def build():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secret"
    return app

# if __name__ == '__main__':
#     app = build()
#     app.run(debug=True)