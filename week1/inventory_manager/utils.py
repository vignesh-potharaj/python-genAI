def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()

        if choice in ("y", "n"):
            return choice
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def print_decorator(func): #args, kwargs, decorators
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
    return wrapper
