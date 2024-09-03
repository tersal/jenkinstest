from flask import Flask

my_app = Flask(__name__)

@my_app.route("/")
def main_access():
    return "<h1>It Works</h1>"


if __name__ == '__main__':
    my_app.run(host='0.0.0.0', port=5000)