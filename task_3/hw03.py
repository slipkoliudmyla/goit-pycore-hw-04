
import sys
from pathlib import Path
from colorama import Fore, Style, init
init()

if len(sys.argv) < 2:
    print("Передайте шлях до директорії")
    sys.exit()

path = Path(sys.argv[1])
if not path.exists():
    print("Такий шлях не існує")
    sys.exit()

if not path.is_dir():
    print("Це не директорія")
    sys.exit()

def print_tree(path, level=0):
    indent = "  " * level

    for item in path.iterdir():
        if item.is_dir():
            print(indent + Fore.BLUE + "📁 " + item.name + Style.RESET_ALL)
            print_tree(item, level + 1)
        else:
            print(indent + Fore.GREEN + "📄 " + item.name + Style.RESET_ALL)

print(Fore.BLUE + "📦 " + path.name + Style.RESET_ALL)
print_tree(path)

