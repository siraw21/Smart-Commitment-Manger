from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Task
from app.services.task_service import calculate_priority

task_bp = Blueprint("task_bp", __name__)

# CREATE TASK
@task_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()

    new_task = Task(
        title=data['title'],
        importance=data['importance'],
        urgency=data['urgency'],
        estimated_time=data['estimated_time'],
        user_id=data.get('user_id')
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message": "Task created"}), 201


# GET TASKS WITH PRIORITY
@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()

    result = []

    for task in tasks:
        priority = calculate_priority(task)

        result.append({
            "id": task.id,
            "title": task.title,
            "priority": priority
        })

    # Sort by priority (MOST IMPORTANT PART)
    result = sorted(result, key=lambda x: x['priority'], reverse=True)

    return jsonify(result)