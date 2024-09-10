from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import time

app = Flask(__name__)

# Function to get a database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    activities = conn.execute('SELECT * FROM activities').fetchall()
    conn.close()
    return render_template('ActivityTracker.html', activities=activities)

@app.route('/add_activity', methods=['POST'])
def add_activity():
    name = request.form['name']
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    duration = request.form['duration']
    
    conn = get_db_connection()
    conn.execute("INSERT INTO activities (name, start_time, end_time, duration) VALUES (?, ?, ?, ?)",
                 (name, start_time, end_time, duration))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/activities_for_date', methods=['POST'])
def activities_for_date():
    date = request.form['date']
    conn = get_db_connection()
    activities = conn.execute("SELECT * FROM activities WHERE start_time LIKE ?", (date + '%',)).fetchall()
    conn.close()
    return render_template('ActivityTracker.html', activities=activities)

@app.route('/current_activity', methods=['GET'])
def current_activity():
    # Example current activity
    current_activity = {
        'name': 'Example Activity',
        'start_time': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    return jsonify(current_activity)

if __name__ == '__main__':
    app.run(debug=True)