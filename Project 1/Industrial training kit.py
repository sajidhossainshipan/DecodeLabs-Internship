def main():
    tasks = []

    while True:
        print("\nTo-Do List Menu")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ").strip()
            if task:
                tasks.append(task)
                print("Task added.")
            else:
                print("Task cannot be empty.")
        elif choice == "2":
            if tasks:
                print("\nYour tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
            else:
                print("No tasks yet.")
        elif choice == "3":
            if tasks:
                print("\nYour tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                index = input("Enter the task number to delete: ")
                if index.isdigit() and 1 <= int(index) <= len(tasks):
                    removed = tasks.pop(int(index) - 1)
                    print(f"Deleted: {removed}")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks yet.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()