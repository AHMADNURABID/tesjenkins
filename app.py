from flask import Flask
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pengunjung (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def hello():
    init_db()
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pengunjung (nama) VALUES ('Mahasiswa Komputasi Awan')")
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM pengunjung")
    jumlah = cursor.fetchone()[0]
    conn.close()

    return f"Halo! Berhasil terhubung ke Database. Total pengunjung tercatat: {jumlah}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
