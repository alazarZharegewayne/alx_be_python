def set_reminder():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            urgency = "requires immediate attention today!"
        case "medium":
            urgency = "should be completed soon."
        case "low":
            urgency = "consider completing it when you have free time."
        case _:
            urgency = "has unspecified priority."

    if time_bound == "yes":
        urgency = urgency.replace("soon", "immediate attention today")
        urgency = urgency.replace("consider", "requires")

    print(f"\nReminder: '{task}' is a {priority} priority task {urgency}")

if __name__ == "__main__":
    set_reminder()