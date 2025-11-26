
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS tutors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    created_at TEXT
);

CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    code TEXT UNIQUE,
    program TEXT,
    created_at TEXT
);

CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tutor_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    notes TEXT,
    created_at TEXT,
    FOREIGN KEY(tutor_id) REFERENCES tutors(id),
    FOREIGN KEY(student_id) REFERENCES students(id)
);
