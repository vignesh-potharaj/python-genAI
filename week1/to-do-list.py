tasks = [
    "complete my homework",
    "wash the dishes",
    "dry the clothes",
    "take the dog for a walk"
]

def to_do_list():
    while True:
        print("""
                        WELCOME TO YOUR TO-DO-LIST APPP
                        1. VIEW TASKS
                        2. ADD A TASK
                        3. REMOVE A TASK
                        4. SAVE TO A FILE
                        5. EXIT""")
        action_map = {
            1: display_list,
            2: add_to_list,
            3: remove_from_list,
            4: save_to_file
        }
        try:
            action = int(input("enter a number to select an action "))

            if 1 <=action <= 4:
                if action == 5:
                    print("exiting..............")
                    break
                action_map[action]()
            else:
                print("enter a number from 1 to 3")

        except ValueError:
            print("please enter a valid number")

def display_list():
    for task in tasks:
        print(f"{tasks.index(task) + 1}.{task}")

def add_to_list():
    for task in tasks:
        print(f"{tasks.index(task) + 1}.{task}")
    task_to_add = input("enter the task to add ")
    tasks.append(task_to_add)
    print("\n task Successfully added")

    for task in tasks:
        print(f"{tasks.index(task) + 1}.{task}")

def remove_from_list():
    for task in tasks:
        print(f"{tasks.index(task) + 1}.{task}")
    task_to_remove = int(input("select a task to remove "))
    tasks.pop(task_to_remove - 1)
    print("\n task Successfully Removed \n")

    for task in tasks:
        print(f"{tasks.index(task) + 1}.{task}")


def save_to_file():
    file_name = input("enter the filename(default name is todo.txt)").strip()
    if not file_name:
        file_name = "todo.txt"
    
    try:
        with open(file_name, 'w') as file:
            for task in tasks:
                file.write(f"{task} \n")
            print(f"tasks successfully saved to {file_name}")
    except:
        print("error saving the file")


if __name__ == "__main__":
    to_do_list()