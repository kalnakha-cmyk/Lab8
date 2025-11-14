import random
from rich.console import Console
from rich import print
from adventure.utils import read_events_from_file

console = Console()


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
    events = read_events_from_file("events.txt")

    print("You wake up in a dark forest. You can go [red] left [/red] or [blue] right [/blue].")

    while True:

        # MUST use console.print so bold becomes ANSI escape codes
        console.print("[bold]Which direction do you choose? (left/right) or (exit): [/bold] ", end="")

        choice = input().strip().lower()

        if choice == "left":
            print(left_path(random.choice(events)))

        elif choice == "right":
            print(right_path(random.choice(events)))

        elif choice == "exit":
            console.print("[bold green]Goodbye![/bold green]")
            break

        else:
            print("That's not a valid choice.")

