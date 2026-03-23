def calculate_priority(task):
    return round((task.importance * task.urgency) / task.estimated_time, 2)


# def generate_daily_plan(tasks, available_minutes):
#     # Step 1: calculate priority for each task
#     task_with_priority = []

#     for task in tasks:
#         priority = calculate_priority(task)
#         # priority = (task.importance * task.urgency) / task.estimated_time
#         task_with_priority.append((task, priority))

#     # Step 2: sort by priority (highest first)
#     task_with_priority.sort(key=lambda x: x[1], reverse=True)

#     # Step 3: fill time
#     plan = []
#     used_time = 0

#     for task, priority in task_with_priority:
#         if used_time + task.estimated_time <= available_minutes:
#             plan.append({
#                 "title": task.title,
#                 "estimated_time": task.estimated_time,
#                 "priority": priority
#             })
#             used_time += task.estimated_time

#     return plan

# Replaced version
def generate_daily_plan(tasks, available_minutes, energy_level):
    task_with_priority = []

    for task in tasks:
        priority = calculate_priority(task)

        # Adjust priority based on energy
        if energy_level == "low" and task.importance >= 4:
            priority *= 0.5  # avoid heavy tasks

        elif energy_level == "high":
            priority *= 1.2  # encourage difficult tasks

        task_with_priority.append((task, priority))

    # Sort
    task_with_priority.sort(key=lambda x: x[1], reverse=True)

    # Build plan
    plan = []
    used_time = 0

    for task, priority in task_with_priority:
        if used_time + task.estimated_time <= available_minutes:
            plan.append({
                "title": task.title,
                "estimated_time": task.estimated_time,
                "priority": priority
            })
            used_time += task.estimated_time

    return plan