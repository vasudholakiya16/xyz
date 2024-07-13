from datetime import datetime

# Define the tasks with start and end dates
tasks = [
    {"name": "Task A", "start_date": "2024-07-01", "end_date": "2024-07-05"},
    {"name": "Task B", "start_date": "2024-07-04", "end_date": "2024-07-10"},
    {"name": "Task C", "start_date": "2024-07-06", "end_date": "2024-07-08"},
    {"name": "Task D", "start_date": "2024-07-11", "end_date": "2024-07-15"}
]

# Convert string dates to datetime objects
for task in tasks:
    task["start_date"] = datetime.strptime(task["start_date"], "%Y-%m-%d")
    task["end_date"] = datetime.strptime(task["end_date"], "%Y-%m-%d")

# Sort tasks by start date (and end date for tie-breaking)
tasks.sort(key=lambda x: (x["start_date"], x["end_date"]))

# Initialize paths
paths = []

# Function to check if a task overlaps with the last task in a path
def overlaps(last_task, new_task):
    return new_task["start_date"] <= last_task["end_date"]

# Distribute tasks into independent paths
for task in tasks:
    placed = False
    for path in paths:
        if not overlaps(path[-1], task):
            path.append(task)
            placed = True
            break
    if not placed:
        paths.append([task])

# Display the result
for i, path in enumerate(paths, 1):
    print(f"Path {i}:")
    for task in path:
        print(f"  {task['name']} ({task['start_date'].strftime('%Y-%m-%d')} to {task['end_date'].strftime('%Y-%m-%d')})")
