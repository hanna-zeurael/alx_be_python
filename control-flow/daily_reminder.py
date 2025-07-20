task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")

match priority.lower():
    case "high":
        if time.lower() == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to complete it soon.")
    case "medium":
        if time.lower() == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be done today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Plan to do it this week.")
    case "low":
        if time.lower() == "yes":
            print(f"Reminder: '{task}' is a low priority task, but time-sensitive. Don't forget to do it today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Unknown priority entered. Please use 'high', 'medium', or 'low'.")