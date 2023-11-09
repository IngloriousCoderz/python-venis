from ..model.task import Task

tasks = [
    Task(id=1, text='Learn Python', completed=True),
    Task(id=2, text='Look for a job', completed=False),
    Task(id=3, text='Forget everything', completed=False),
]


def read_tasks():
    return [task.serialize() for task in tasks]


def read_task(id):
    return next(task for task in tasks if task['id'] == id)


def create_task(new_task):
    max_id = tasks[len(tasks) - 1]['id'] if len(tasks) else 0
    new_task['id'] = max_id + 1
    tasks.append(new_task)
    return new_task, 201


def replace_task(id, new_task):
    new_task['id'] = id
    index = next(index for index, task in enumerate(
        tasks) if task['id'] == id)
    tasks[index] = new_task
    return new_task


def update_task(id, patch):
    updated_task = read_task(id)
    updated_task.update(patch)
    return updated_task


def delete_task(id):
    deleted_task = read_task(id)
    tasks.remove(deleted_task)
    return deleted_task
