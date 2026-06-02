from flask import Flask, request, jsonify, send_from_directory
import Backend as back

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

# CREATE
# CREATE
@app.route('/api/task/add', methods=['POST'])
def add_task():
    task = request.form.get("task")
    day = request.form.get("day")
    date_value = request.form.get("date")
    time_value = request.form.get("time")

    back.add_task(task, day, date_value, time_value)
    return "Added"

# READ ALL
@app.route('/api/task/all', methods=['GET'])
def all_tasks():
    back.auto_reset()
    rows = back.get_all_tasks()
    return jsonify(rows)

# UPDATE
@app.route('/api/task/update', methods=['POST'])
def update():
    task_id = request.form.get("id")
    new_task = request.form.get("task")
    back.update_task(task_id, new_task)
    return "Updated"

# MARK COMPLETE
@app.route('/api/task/complete', methods=['POST'])
def complete():
    task_id = request.form.get("id")
    back.mark_complete(task_id)
    return "Completed"

# DELETE
@app.route('/api/task/delete', methods=['POST'])
def delete():
    task_id = request.form.get("id")
    back.delete_task(task_id)
    return "Deleted"

# RESET
@app.route('/api/task/reset', methods=['POST'])
def reset():
    task_id = request.form.get("id")
    back.reset_by_id(task_id)
    return "Reset"

# ✅ SHOW ONLY TODAY'S TASKS
@app.route('/api/task/today', methods=['GET'])
def today_tasks():
    back.auto_reset()
    rows = back.todays()
    return jsonify(rows)
@app.route('/api/task/overdue', methods=['GET'])
def api_overdue():
    data = back.ouverdue()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
