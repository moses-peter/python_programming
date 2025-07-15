import random
from datetime import datetime

# Sample affirmations
affirmations = [
    "I am capable of achieving great things.",
    "Today is a fresh start.",
    "I radiate positivity.",
    "I choose peace over worry.",
    "I am learning and growing every day."
]

def get_user_input():
    mood = input("How are you feeling today? 😌: ")
    print("\nChoose one:")
    print("1. Get a random affirmation")
    print("2. Write my own affirmation")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        affirmation = random.choice(affirmations)
        print("✨ Your affirmation:", affirmation)
    elif choice == "2":
        affirmation = input("Write your own affirmation: ")
    else:
        print("Invalid choice. Using default affirmation.")
        affirmation = "I am growing, learning, and evolving daily."
    
    return mood, affirmation

def save_journal_entry(mood, affirmation):
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"[{today}] Mood: {mood} | Affirmation: {affirmation}\n"
    
    with open("journal.txt", "a") as file:
        file.write(entry)
    
    print("✅ Entry saved!\n")

def view_journal():
    print("\n📝 Past Journal Entries:")
    try:
        with open("journal.txt", "r") as file:
            logs = file.readlines()
            if logs:
                for line in logs:
                    print(line.strip())
            else:
                print("No journal entries yet.")
    except FileNotFoundError:
        print("No journal file found yet.\n")

def main():
    while True:
        print("\n📘 Daily Affirmation Journal")
        print("1. Add new entry")
        print("2. View past entries")
        print("3. Exit")

        option = input("Choose an option: ")

        if option == "1":
            mood, affirmation = get_user_input()
            save_journal_entry(mood, affirmation)
        elif option == "2":
            view_journal()
        elif option == "3":
            print("Goodbye, stay positive! 🌞")
            break
        else:
            print("Invalid choice, try again.")

# Run the app
main()
