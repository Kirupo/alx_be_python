# daily_reminder.py

# Get task details from the user
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to customize reminder by priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"Task priority '{priority}' is not recognized."

# If time-bound and priority is high or medium, add urgency
if time_bound == "yes" and priority in ("high", "medium"):
    reminder += " that requires immediate attention today!"

print(reminder)
