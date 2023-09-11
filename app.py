from flask import Flask,render_template,request,url_for ,send_from_directory
import os

app = Flask(__name__)
# Define the folder where uploaded files are stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

users =[
    {"user_name":"waga","pwd":"123"},
    {"user_name":"baga","pwd":"456"}
]

@app.route('/test')
def test():
    return render_template('main.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/start')
def index():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)  # Save the uploaded file to the 'uploads' folder
        return f"File '{filename}' uploaded successfully. <a href='/uploads/{filename}'>View Image</a>"



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route("/",methods=["get","post"])
def hello_world():
    pwd= request.form.get("pwd") 
    user_name= request.form["user"]
    found =False
    for usr in users:
        if usr["user_name"] ==  user_name and usr["pwd"]==pwd: found =True
    if found:
        return render_template("welc.html",msg=user_name) 
    else:
        return render_template("index.html",msg="") 

if __name__ == "__main__":
    app.run(debug=True, port=7000)