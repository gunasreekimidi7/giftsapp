from flask import Flask, render_template, request, jsonify
import os
import psycopg2

app = Flask(__name__)

# Connect PostgreSQL using Render Environment Variable
DATABASE_URL = os.environ.get("postgresql://lucky_gits_user:23PaLy5szgW5I2AaiTLrJS6HmByfy3Hk@dpg-d65ggol6ubrc7394esug-a/lucky_gits")

db = psycopg2.connect(DATABASE_URL)
cursor = db.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_gift', methods=['POST'])
def get_gift():
    number = request.json['number']

    cursor.execute(
        "SELECT gift_name FROM gifts WHERE id = %s",
        (number,)
    )
    result = cursor.fetchone()

    if result:
        return jsonify({"gift": result[0]})
    else:
        return jsonify({"gift": "No Gift Found"})

if __name__ == '__main__':
    app.run()
