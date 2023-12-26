from flask import Flask, Blueprint, render_template

app = Flask(__name__)
blueprint = Blueprint('my_blueprint', __name__, static_folder='static')

@app.route('/')
def index():
    return render_template('proyekakhir.html')

app.register_blueprint(blueprint, url_prefix='/my_blueprint')

if __name__ == '__main__':
    app.run(debug=True)
