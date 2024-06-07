from flask import Flask , render_template ,request,redirect
import subprocess
from imgix import UrlBuilder

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/robot")
def robot():
    return render_template("robot.html")

@app.route('/chat')
def index():
    return render_template('index.html')

@app.route('/games')
def games():
    #sudo apt install florence
    # subprocess.run('florence', shell=True)
    return render_template('games.html')

@app.route("/photo")
def photo():
    # subprocess.run('rpicam-jpeg --output /static/test.jpg', shell=True)
    ub = UrlBuilder("demo.imgix.net")
    print(ub.create_url("test.jpg", {'w': 100, 'h': 100}))
    return render_template("photo.html")


if __name__ =="__main__": 
    # import webbrowser
    # webbrowser.open_new("http://127.0.0.1:5000")
    app.run(debug=True)