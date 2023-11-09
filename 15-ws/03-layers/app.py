from flask import Flask, request

from ws.service import fake_db as db

app = Flask(__name__)


# with app.app_context():
#     db.create_tasks()


@app.get("/tasks")
def read_tasks():
    return db.read_tasks()


@app.post("/tasks")
def create_task():
    return db.create_task(request.json)


@app.patch("/tasks/<int:id>")
def update_task(id):
    return db.update_task(id, request.json)


@app.delete("/tasks/<int:id>")
def delete_task(id):
    return db.delete_task(id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
