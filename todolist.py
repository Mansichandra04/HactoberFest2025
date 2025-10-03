tasks = []

def show_tasks():
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")
    if not tasks: print("No tasks yet!")

while True:
    cmd = input("\n[add/show/quit] > ").strip().lower()
    if cmd == "add":
        tasks.append(input("Enter task: "))
    elif cmd == "show":
        show_tasks()
    elif cmd == "quit":
        break
    else:
        print("Invalid command!")
