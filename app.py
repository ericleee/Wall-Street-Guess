from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__, template_folder='templates')

# Connect to the database 
conn = psycopg2.connect(database="StockGuess", user="edward", 
                        password="x", host="localhost", port="5432") 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    conn = psycopg2.connect(database="StockGuess", user="edward", 
                        password="x", host="localhost", port="5432") 
    cur = conn.cursor()

    email = request.form['email']
    password = request.form['pswd']

    cur.execute("SELECT password FROM users WHERE email=%s", (email,))

    row = cur.fetchall()

    if row[0][0] == password:
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/about.html')
def about():
    return render_template('about.html')    

if __name__ == '__main__':
    app.run(debug=True)