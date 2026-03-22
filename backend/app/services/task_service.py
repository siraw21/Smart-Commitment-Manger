def calculate_priority(task):
    
    return round((task.importance * task.urgency) / task.estimated_time, 2)