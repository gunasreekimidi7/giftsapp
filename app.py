from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Connect MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="WJ28@krhps",
    database="giftsdb"
)

cursor = db.cursor()

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/get_gift', methods=['POST'])
def get_gift():
    number = request.json['number']

    cursor.execute("SELECT gift_name FROM gifts WHERE id=%s", (number,))
    result = cursor.fetchone()

    if result:
        return jsonify({"gift": result[0]})
    else:
        return jsonify({"gift": "No Gift Found"})

if __name__ == '__main__':
    app.run(debug=True)
