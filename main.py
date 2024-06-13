from flask import Flask , render_template ,request ,redirect ,flash
import subprocess
import time
import pyimgur
import os
from werkzeug.utils import secure_filename
from pymongo import MongoClient
import re
from datetime import datetime


CLIENT_ID = "34982a924cfeb95"
im = pyimgur.Imgur(CLIENT_ID)

client = MongoClient('mongodb+srv://rajanpoudelnp:HJjU4sEeDNVzOpgL@rajancluster.rpt2ua9.mongodb.net/?retryWrites=true&w=majority&appName=RajanCluster')

app = Flask(__name__)
app.config['Upload_Folder'] = '/home/ankuram/AnkuramRobot/static/Upload_Folder'
app.secret_key="supersecretkeydkdjd"

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/robot")
def robot():
    return render_template("robot.html")

@app.route('/chat')
def index():
    return render_template('index.html')

@app.route('/other')
def other():
    return render_template('games.html')

@app.route('/other2')
def other2():
    return render_template('games2.html')

@app.route('/virtualtour')
def virtualtour():
    return render_template('virtualtour.html')

@app.route('/navigation')
def navigation():
    return render_template('navigation.html')

@app.route('/emergency')
def emergency():
    return render_template('emergency.html')

@app.route('/gamesfinal')
def gamesfinal():
    return render_template('gamesfinal.html')

@app.route('/scribble')
def scribble():
    return render_template('scribble.html')

@app.route('/carball')
def carball():
    return render_template('carball.html')

@app.route('/suduko')
def suduko():
    return render_template('suduko.html')

@app.route('/codenames')
def codenames():
    return render_template('codenames.html')

@app.route('/chess')
def chess():
    return render_template('chess.html')

@app.route('/bingo')
def bingo():
    return render_template('bingo.html')


@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/menu", methods=['GET', 'POST'])
def menu():
    db = client["foodmenu"]
    collection = db["foodmenu"]
    document = collection.find_one({"user": "root"})
    url = document.get("foodmenu_url")
    url = url.split("?usp=sharing")[0]
    url = url.replace("/view", "/preview")
    return render_template('menu.html',url=url)
    
@app.route("/slides", methods=['GET', 'POST'])
def slide():
    db = client["slide"]
    collection = db["slide"]
    document = collection.find_one({"user": "root"})
    url = document.get("slide_url")
    return render_template('slide.html',url=url)
    
@app.route("/notice", methods=['GET', 'POST'])
def notice():
    db = client["notice"]
    collection = db["notice"]
    document = collection.find_one({"user": "root"})
    url = document.get("notice_url")
    url = url.split("?usp=sharing")[0]
    url = url.replace("/view", "/preview")
    return render_template('notice.html',url=url)

@app.route("/photo")
def photo():
    a = int(time.time())
    subprocess.run(f'rpicam-jpeg --output static/captures/{a}.jpeg', shell=True)
    return render_template("photo.html",photo_name=f'captures/{a}.jpeg')
    #return render_template("photo.html",photo_name=f'captures/test.jpg')

@app.route("/share", methods=["POST"])
def share():
    photo_name = request.form.get("photo_name")
    photo_path = f"./static/{photo_name}"
    uploaded_image = im.upload_image(photo_path, title="Ankuram Robot 2081")
    url = uploaded_image.link
    return render_template("share.html",url=url)

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/thinggot", methods=['GET', 'POST'])
def thinggot():
    if request.method == "POST":
        db = client["thingfinder"]
        collection = db["thingfinder"] 
        phone = request.form.get("phone")
        thinggot = request.form.get("thinggot")
        file = request.files['file']
        file.save(os.path.join(app.config['Upload_Folder'],secure_filename(f"{thinggot}.png")))
        user_data = {
    "phone": phone,
    "thinggot":thinggot,
    "date": datetime.now()
}
        result = collection.insert_one(user_data)
        flash("Your data is submitted","success")
        return redirect('/search')
        

@app.route("/thinglost", methods=['GET', 'POST'])
def thinglost():
    if request.method == "POST":
        db = client["thingfinder"]
        collection = db["thingfinder"]
        phone = request.form.get("phone")
        thinglost = request.form.get("thinglost")
        pattern = re.compile(re.escape(thinglost), re.IGNORECASE)
        results = db["thingfinder"].find({"thinggot": pattern})
        return render_template('found.html', results=results)  
    return redirect("/search")


if __name__ =="__main__": 
    #import webbrowser
    #webbrowser.open_new("http://127.0.0.1:5000")
    app.run(debug=True)
