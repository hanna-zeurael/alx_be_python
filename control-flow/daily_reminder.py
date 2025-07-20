
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")


match priority.lower():
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task."
    case _:
        reminder = "Unknown priority level entered."

if time_bound.lower() == "yes" and priority.lower() in ["high", "medium", "low"]:
    reminder += " It is time-bound and **that requires immediate attention today!**"


print(reminder)
