
import random

# This list stores all tasks entered by the user.
tasks = []


# TOOL 1: SIMPLE CALCULATOR
# This tool allows users to perform basic mathematical calculations.
def calculator():
    print("\n--- SIMPLE CALCULATOR ---")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Enter your choice (1-4): ")

        if operation == "1":
            result = num1 + num2
            print(f"The answer is: {result}")

        elif operation == "2":
            result = num1 - num2
            print(f"The answer is: {result}")

        elif operation == "3":
            result = num1 * num2
            print(f"The answer is: {result}")

        elif operation == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"The answer is: {result}")
            else:
                print("Sorry! Division by zero is not allowed.")

        else:
            print("Invalid operation. Please try again.")

    except ValueError:
        print("Please enter valid numbers.")


# TOOL 2: NUMBER GUESSING GAME
# This tool asks users to guess a random number between 1 and 10.
def guessing_game():
    print("\n--- NUMBER GUESSING GAME ---")

    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue

            attempts += 1

            if guess == secret_number:
                print(f"Congratulations! You guessed correctly!")
                print(f"You took {attempts} attempts.")
                break

            elif guess < secret_number:
                print("Too low! Try again.")

            else:
                print("Too high! Try again.")

        except ValueError:
            print("Please enter a valid whole number.")


# TOOL 3: TO-DO LIST MANAGER
# This tool allows users to add, view, and remove tasks.
def todo_list():
    while True:
        print("\n--- TO-DO LIST MANAGER ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter your task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task '{task}' added successfully!")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYOUR TASKS:")

                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(
                        input("Enter the task number to remove: ")
                    )

                    if 1 <= task_number <= len(tasks):
                        removed = tasks.pop(task_number - 1)
                        print(f"Task '{removed}' removed successfully!")
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice. Please try again.")


# TOOL 4: NAME FORMATTER
# This tool displays a name in uppercase, lowercase, and title case.
def name_formatter():
    print("\n--- NAME FORMATTER ---")

    name = input("Enter your full name: ").strip()

    if name:
        print(f"Uppercase: {name.upper()}")
        print(f"Lowercase: {name.lower()}")
        print(f"Title case: {name.title()}")
    else:
        print("Please enter a valid name.")


# MAIN MENU
# This function controls the program and keeps the menu running.
def main():

    print("\n========================================")
    print("   WELCOME TO MY PERSONAL MINI-TOOLKIT")
    print("========================================")
    print("Your collection of useful Python tools!")

    while True:
        print("\n========================================")
        print("       MY PERSONAL MINI-TOOLKIT")
        print("========================================")
        print("1. Simple Calculator")
        print("2. Number Guessing Game")
        print("3. To-Do List Manager")
        print("4. Name Formatter")
        print("5. Quit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            calculator()

        elif choice == "2":
            guessing_game()

        elif choice == "3":
            todo_list()

        elif choice == "4":
            name_formatter()

        elif choice == "5":
            print("\nThank you for using my toolkit!")
            print("Keep learning Python. Goodbye!")
            break

        else:
            print(f"Sorry, '{choice}' is not a valid choice.")
            print("Please select a number between 1 and 5.")


# Start the program.
if __name__ == "__main__":
    main()
