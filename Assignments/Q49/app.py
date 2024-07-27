from flask import Flask, render_template, request, redirect, url_for, session
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MongoDB configuration
uri = "mongodb+srv://rithin:rithin@mlproject.urgc7pj.mongodb.net/?retryWrites=true&w=majority&appName=mlproject"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.mlproject
collections = db.users

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('welcome'))
    return redirect(url_for('signin'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        
        collections.insert_one({'username': username, 'password': hashed_password})
        return redirect(url_for('signin'))
    
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = collections.find_one({'username': username})
        
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('welcome'))
    
    return render_template('signin.html')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    return redirect(url_for('signin'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)
