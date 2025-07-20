def set_reminder():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            if time_bound == "yes":
                print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"\nReminder: '{task}' is a high priority task.")
        case "medium":
            if time_bound == "yes":
                print(f"\nReminder: '{task}' is a medium priority task that requires immediate attention today!")
            else:
                print(f"\nNote: '{task}' is a medium priority task.")
        case "low":
            if time_bound == "yes":
                print(f"\nReminder: '{task}' is a low priority task that requires immediate attention today!")
            else:
                print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print("\nInvalid priority level entered.")

if __name__ == "__main__":
    set_reminder()