from flask import Flask, render_template, request, abort

app = Flask(__name__)

tasks = [
    {'id': 1, 'text': 'Learn Python', 'completed': True},
    {'id': 2, 'text': 'Look for a job', 'completed': False},
    {'id': 3, 'text': 'Forget everything'},
]


@app.get("/tasks")
def read_tasks():
    return tasks


@app.get("/tasks/<int:id>")
def read_task(id):
    try:
        return next(task for task in tasks if task['id'] == id)
    except StopIteration:
        app.logger.warning("Task %d not found", id)
        abort(404)


@app.post("/tasks")
def create_task():
    new_task = request.json
    max_id = tasks[len(tasks) - 1]['id'] if len(tasks) else 0
    new_task['id'] = max_id + 1
    tasks.append(new_task)
    return new_task, 201


@app.put("/tasks/<int:id>")
def replace_task(id):
    new_task = request.json
    new_task['id'] = id
    try:
        index = next(index for index, task in enumerate(
            tasks) if task['id'] == id)
        tasks[index] = new_task
        return new_task
    except StopIteration:
        app.logger.warning("Task %d not found", id)
        abort(404)


@app.patch("/tasks/<int:id>")
def update_task(id):
    patch = request.json
    updated_task = read_task(id)
    updated_task.update(patch)
    return updated_task


@app.delete("/tasks/<int:id>")
def delete_task(id):
    deleted_task = read_task(id)
    tasks.remove(deleted_task)
    return deleted_task


@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html'), 404
