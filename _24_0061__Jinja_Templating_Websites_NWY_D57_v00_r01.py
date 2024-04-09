
from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    return render_template('index_server_NWY_D57_v00_r01.html', greeting_string="Hello Jinja!", num=random_number)


if __name__ == "__main__":
    app.run(debug=True)