import os
import time

offset = ' '
line = ' '
colors = [7, 3, 4]
while True:
    for color in colors:
        print(f'{offset * 8}\x1b[48;5;{color}m{line * 8}\x1b[0m{offset * 12}\x1b[48;5;{color}m{line * 8}\x1b[0m')
        print(f'{offset * 6}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 4}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 8}\x1b[48;5;{color}m{line * 4}\x1b[0m\x1b[0m{offset * 4}\x1b[48;5;{color}m{line * 4}\x1b[0m')
        print(f'{offset * 4}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 8}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 4}\x1b[48;5;{color}m{line * 4}\x1b[0m\x1b[0m{offset * 8}\x1b[48;5;{color}m{line * 4}\x1b[0m')
        print(f'{offset * 2}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 12}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 0}\x1b[48;5;{color}m{line * 4}\x1b[0m\x1b[0m{offset * 12}\x1b[48;5;{color}m{line * 4}\x1b[0m')
        print(f'{offset * 4}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 8}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 4}\x1b[48;5;{color}m{line * 4}\x1b[0m\x1b[0m{offset * 8}\x1b[48;5;{color}m{line * 4}\x1b[0m')
        print(f'{offset * 6}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 4}\x1b[48;5;{color}m{line * 4}\x1b[0m{offset * 8}\x1b[48;5;{color}m{line * 4}\x1b[0m\x1b[0m{offset * 4}\x1b[48;5;{color}m{line * 4}\x1b[0m')
        print(f'{offset * 8}\x1b[48;5;{color}m{line * 8}\x1b[0m{offset * 12}\x1b[48;5;{color}m{line * 8}\x1b[0m')

        time.sleep(1)
        os.system("cls")