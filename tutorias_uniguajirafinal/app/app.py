
from flask import Flask, render_template, request, redirect, url_for, send_file
import sqlite3, os
from datetime import datetime

DB = os.path.join(os.path.dirname(__file__), "tutorias.db")

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.executescript(open(os.path.join(os.path.dirname(__file__), "schema.sql")).read())
    conn.commit()
    conn.close()

app = Flask(__name__)

@app.route("/")
def index():
    conn = get_db()
    tutors = conn.execute("SELECT * FROM tutors").fetchall()
    students = conn.execute("SELECT * FROM students").fetchall()
    sessions = conn.execute("SELECT s.id, s.date, s.notes, t.name as tutor, st.name as student FROM sessions s JOIN tutors t ON s.tutor_id=t.id JOIN students st ON s.student_id=st.id ORDER BY s.date DESC").fetchall()
    conn.close()
    return render_template("index.html", tutors=tutors, students=students, sessions=sessions)

@app.route("/init")
def init():
    if not os.path.exists(DB):
        init_db()
        return "Base de datos inicializada. <a href='/'>Ir a inicio</a>"
    return "La base de datos ya existe. <a href='/'>Ir a inicio</a>"

@app.route("/tutor/add", methods=["POST"])
def add_tutor():
    name = request.form.get("name")
    email = request.form.get("email")
    conn = get_db()
    conn.execute("INSERT INTO tutors(name,email,created_at) VALUES (?,?,?)", (name,email,datetime.utcnow()))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

@app.route("/student/add", methods=["POST"])
def add_student():
    name = request.form.get("name")
    code = request.form.get("code")
    program = request.form.get("program")
    conn = get_db()
    conn.execute("INSERT INTO students(name,code,program,created_at) VALUES (?,?,?,?)", (name,code,program,datetime.utcnow()))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

@app.route("/session/add", methods=["POST"])
def add_session():
    tutor_id = request.form.get("tutor_id")
    student_id = request.form.get("student_id")
    date = request.form.get("date")
    notes = request.form.get("notes")
    conn = get_db()
    conn.execute("INSERT INTO sessions(tutor_id,student_id,date,notes,created_at) VALUES (?,?,?,?,?)", (tutor_id,student_id,date,notes,datetime.utcnow()))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

@app.route("/export/sql")
def export_sql():
    return send_file(DB, as_attachment=True, download_name="tutorias.db")

if __name__ == "__main__":
    app.run(debug=True)
