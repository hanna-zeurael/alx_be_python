task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task."
    case _:
        reminder = "Unknown priority entered. Please use 'high', 'medium', or 'low'."

# Add time-sensitive message
if priority in ("high", "medium", "low") and time == "yes":
    reminder += " It requires immediate attention today!"

print(reminder)
