#Importing libraries
from flask import Flask , render_template ,request,redirect
import webbrowser
import google.generativeai as genai

#Gemini
model = genai.GenerativeModel('gemini-pro')
genai.configure(api_key="AIzaSyBhG8sdo4Z0921mEZ6U8I5D1D4kX6QaV3A")

# Automatic opening in browser
# url = ""
# webbrowser.open(url)

#Flask app
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/robot")
def robot():
    return render_template("robot.html")

@app.route('/chat', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            prompt = request.form['prompt']
            question = prompt 
            response = model.generate_content(question)

            if response.text:
                return response.text
            else:
                return "Sorry, but I think Gemini didn't want to answer that!"
        except Exception as e:
            return "Sorry, but Gemini didn't want to answer that!"

    return render_template('index.html', **locals())

@app.route("/photo")
def photo():
    return render_template("photo.html")

if __name__ =="__main__": 
    webbrowser.open_new("http://127.0.0.1:5000")
    app.run(debug=True)