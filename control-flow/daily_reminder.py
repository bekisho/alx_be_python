# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Start building the reminder message
reminder = f"Reminder: '{task}' is a"

# Use match-case for priority message
match priority:
    case "high":
        reminder += " high priority task"
    case "medium":
        reminder += " medium priority task"
    case "low":
        reminder += " low priority task"
    case _:
        reminder += " task with unspecified priority"

# Add time-sensitivity information
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += "."

# Print the final reminder message
print("\n" + reminder)

