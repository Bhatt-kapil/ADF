from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Yuki_8686009',
        database='sekai'
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student")
    users = cursor.fetchall()
    conn.close()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)