from termcolor import colored
import pyfiglet
import time
from datetime import datetime

def print_colored_message(message, color):
    print(colored(message, color))

def birthday_message(name):
    ascii_art = pyfiglet.figlet_format(f"Advance \nHappy Birth \nday \n{name} !", font="starwars")

    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

    for i, line in enumerate(ascii_art.splitlines()):
        color = colors[i % len(colors)]
        print_colored_message(line, color)
        time.sleep(0.5)

    current_year = datetime.now().year
    print_colored_message("\n\033[1mWishing you a fantastic year ahead filled with joy, success, and good health.\033[0m", 'cyan')
    print_colored_message("\n\033[1mEnjoy your special day and make the most of every moment!\033[0m", 'yellow')
    print_colored_message(f"\n\033[1mCheers to {current_year} being your best year yet!\033[0m\n", 'green')

def countdown(seconds):
    print(colored("\033[1mGet ready for a surprise in...\033[0m", 'yellow'))
    for i in range(seconds, 0, -1):
        print(colored(f"\033[1m{i}...\033[0m", 'cyan'))
        time.sleep(1)

countdown(5)        
if __name__ == "__main__":
    birthday_message("mention a name")
# Mention a name for birthday person 