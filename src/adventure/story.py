from adventure.utils import read_events_from_file
import random
from rich import print

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "You stand still, unsure what to do. The forest swallows you."

def left_path(event):
    return "[red] You walk left [/red]. " + event

def right_path(event):
    return "[blue] You walk right [/blue]. " + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    print("You wake up in a dark forest. You can go [red] left [/red] or [blue] right [/blue].")
    while True:
        choice = input("Which direction do you choose? (left/right) or (exit): ")
        choice = choice.strip().lower()
        if choice == 'exit':
            break
        
        print(step(choice, events))
