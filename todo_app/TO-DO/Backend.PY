import sqlite3
from datetime import datetime, date

def get_connection():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        day TEXT,
        date TEXT,
        time TEXT,
        status TEXT DEFAULT 'pending',
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

    return sqlite3.connect("todo.db")


# CREATE
def add_task(task, day=None, date_value=None, time_value=None):
    conn = get_connection()
    cursor = conn.cursor()

    # If user does not provide values, fill automatically
    if not day or day.strip() == "":
        day = date.today().strftime("%A")   # Monday, Tuesday, etc.

    if not date_value or date_value.strip() == "":
        date_value = date.today().strftime("%Y-%m-%d")

    if not time_value or time_value.strip() == "":
        time_value = datetime.now().strftime("%H:%M:%S")

    cursor.execute("""
        INSERT INTO tasks (task, day, date, time)
        VALUES (?, ?, ?, ?)
    """, (task, day, date_value, time_value))

    conn.commit()
    conn.close()
    return True


def get_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, task, status, day, date, time, created_at FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    conn.close()
    return row


def update_task(task_id, new_task):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET task = ? WHERE id = ?", (new_task, task_id))
    conn.commit()
    conn.close()


def mark_complete(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = 'completed' WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()


def reset_by_id(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = 'pending' WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()


# READ
def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, task, day, date, time, status, created_at FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    return rows


def todays():
    conn = get_connection()
    cursor = conn.cursor()

    today = date.today().strftime("%Y-%m-%d")

    cursor.execute("SELECT id, task, day, date, time, status, created_at FROM tasks WHERE day = ?", (today,))
    rows = cursor.fetchall()

    conn.close()
    return rows


# AUTO STATUS UPDATE
def auto_reset():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, date FROM tasks")
    rows = cursor.fetchall()

    today = date.today()
    
    for task_id, task_date_str in rows:
        task_date = datetime.strptime(task_date_str, "%Y-%m-%d").date()

        if today > task_date:
            cursor.execute("UPDATE tasks SET status = 'pending' WHERE id = ?", (task_id,))
            

    conn.commit()
    conn.close()
from datetime import date, datetime

def ouverdue():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, task, date, status FROM tasks")
    rows = cursor.fetchall()

    today = date.today()
    overdue_list = []  # Store overdue tasks

    for row in rows:
        task_id, task_text, task_date_str, status = row

        if task_date_str:  # Only if date is not empty
            task_date = datetime.strptime(task_date_str, "%Y-%m-%d").date()

            if today > task_date:
                overdue_list.append(row)

    conn.close()
    return overdue_list
