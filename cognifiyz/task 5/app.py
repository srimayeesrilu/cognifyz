from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        try:
            with open(TASK_FILE, "r") as file:
                for line in file:
                    parts = line.strip().split("|")
                    if len(parts) == 5:
                        task_id, name, status, priority, due_date = parts
                        tasks.append({
                            "id": int(task_id),
                            "name": name,
                            "status": status,
                            "priority": priority,
                            "due_date": due_date
                        })
        except IOError:
            print("Error reading tasks file.")
    return tasks

def save_tasks(tasks):
    try:
        with open(TASK_FILE, "w") as file:
            for task in tasks:
                file.write(f"{task['id']}|{task['name']}|{task['status']}|{task['priority']}|{task['due_date']}\n")
    except IOError:
        print("Error writing tasks file.")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    tasks = load_tasks()
    data = request.json
    task_id = max([task["id"] for task in tasks], default=0) + 1
    task = {
        "id": task_id,
        "name": data["name"],
        "status": data["status"],
        "priority": data["priority"],
        "due_date": data["due_date"]
    }
    tasks.append(task)
    save_tasks(tasks)
    return jsonify(task)

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    tasks = load_tasks()
    data = request.json
    for task in tasks:
        if task["id"] == task_id:
            task.update(data)
            save_tasks(tasks)
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    return jsonify({"result": "Task deleted"})

if __name__ == "__main__":
    app.run(debug=True)
