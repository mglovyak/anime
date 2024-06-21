from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def main_for_anime():
    return render_template('main_for_anime.html')





app.run(debug=True)